## A tic-tac-toe AI program.
This program uses the minimax algorithm with alpha-beta pruning to reduce the search space.

Alpha–beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree. This allows us to search much faster and even go into deeper levels in the game tree. It cuts off branches in the game tree which need not be searched because there already exists a better move available. The algorithm maintains two values, alpha and beta, which represent the maximum score that the maximizing player is assured of and the minimum score that the minimizing player is assured of respectively. Initially alpha is negative infinity and beta is positive infinity, i.e. both players start with their lowest possible score. It can happen that when choosing a certain branch of a certain node the minimum score that the minimizing player is assured of becomes less than the maximum score that the maximizing player is assured of (beta <= alpha). If this is the case, the parent node should not choose this node, because it will make the score for the parent node worse. Therefore, the other branches of the node do not have to be explored.

## Pseudocode
![pes](https://user-images.githubusercontent.com/66234085/84352540-36d4a000-abc6-11ea-8ae5-ea52f228aa4e.png)

## Minimax Algorithm Visualisation
![pic](https://user-images.githubusercontent.com/66234085/84352650-6388b780-abc6-11ea-8456-52b7c004fe5e.png)
