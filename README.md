# World Game Solver
There are 2 word games covered in this project:
- Word Search: at each cell as starting cell on the board, try 8 different directions to form words
- Boggle: at each cell, regardless of being the starting cell or not, try 8 different directions to form words
Even though Boggle is more flexible on its way to form words, which also means the algorithm is more complex, the two games share similar base logic: prefix search. Hence, the project utilize a prefix tree (Trie) to solve the game.
