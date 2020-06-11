from copy import copy
import numpy as np


class game():
    board = np.array([['1', '2', '3'],
                      ['4', '5', '6'],
                      ['7', '8', '9']])
    flattenBoard = board.ravel()
    (rows, cols) = board.shape
    turn = " "

    def printboard(self):
        for i in range(self.rows):
          print(self.board[i])

    def getPlayerMove(self):
       # Let the player type in his move.
            p=[1,2,3,4,5,6,7,8,9]
            move = -1
            while move not in p:
              print('What is your next move? (1-9)')
              move = input()
            index = np.where(self.board == str(move) )
            self.board[index] = "X"
            #self.printboard()

    def alphaBeta(self):
        bestval = -1000000
        move = -1
        for i in range(self.flattenBoard.size):
            if(self.flattenBoard[i] != "X" and self.flattenBoard[i] != "O"):
                # for val in arr:
                # print arr
                place = self.flattenBoard[i]
                self.flattenBoard[i] = "O"
                moveval = self.minimax(False, -1000000, 1000000)
                # print arr
                self.flattenBoard[i] = place

                if moveval > bestval:
                    bestval = moveval
                    move = i

        self.flattenBoard[move] = "O"
        self.printboard()

    def minimax(self, isMax, alpha, beta):
        status = self.isWin()
        if (status) :
            if (self.turn == "X") :
                return -10
            else:
                return 10
        elif (self.isBoardFull()):
            return 0

        if (isMax):
            best = -1000000
            for i in range(self.flattenBoard.size):
                if (self.flattenBoard[i] != "X" and self.flattenBoard[i] != "O"):
                    place = self.flattenBoard[i]
                    self.flattenBoard[i] = "O"
                    best = max(best, self.minimax(not isMax, alpha, beta))
                    self.flattenBoard[i] = place
                    alpha = max(alpha, best)
                    # Alpha Beta Pruning
                    if (beta <= alpha):
                        break

            return best

        else:
            best = 1000000
            for i in range(self.flattenBoard.size):
                if (self.flattenBoard[i] != "X" and self.flattenBoard[i] != "O"):
                    place = self.flattenBoard[i]
                    self.flattenBoard[i] = "X"
                    best = min(best, self.minimax(not isMax, alpha, beta))
                    self.flattenBoard[i] = place
                    beta = min(beta, best)
                    # Alpha Beta Pruning
                    if (beta <= alpha):
                        break

            return best


    def isWin(self):
      win = False
      tempH = np.array(self.board)
      tempV = np.array(self.board.T)

      #main diag
      if (self.board[0, 0] == self.board[1, 1] == self.board[2, 2]):
          win = True
          self.turn = self.board[0,0]
          return win

      #reverse diag
      if (self.board[0, 2] == self.board[1, 1] == self.board[2, 0]):
          win = True
          self.turn = self.board[0, 2]
          return win

      for i in range(0, 3):
          # for Horizntal win
          if(tempH[0,i] == tempH[1,i] == tempH[2,i]):
              win = True
              self.turn = tempH[0,i]

          # for vertical win
          if (tempV[0,i] == tempV[1,i] == tempV[2,i]):
              win = True
              self.turn = tempV[0,i]


      return win

    def isBoardFull(self):
      for i in range(self.flattenBoard.size):
        if(self.flattenBoard[i] != "X" and self.flattenBoard[i] != "O"):
          return False
      return True

print('Welcome to Tic Tac Toe!')
g = game()
g.printboard()
notDone=True
turn = "X"

while notDone:
    g.getPlayerMove()
    if (g.isWin()):
        g.printboard()
        print('X, You have won the game!')
        notDone=False
    else:
        turn = "O"
        if (g.isBoardFull()):
          print('The game is a tie!')
          break
        else:
            g.alphaBeta()
            if(g.isWin()):
              print('O, You have won the game!')
              notDone=False
