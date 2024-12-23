# World Game Solver
<p>
  There are 2 word games covered in this project:
<uL>
  <li>Word Search: at each cell as starting cell on the board, try 8 different directions to form words.</li>
  <li>Boggle: at each cell, regardless of being the starting cell or not, try 8 different directions to form words.</li>
</uL>
</p>
<p>
  Even though Boggle is more flexible on its way to form words, which also means the algorithm is more complex, the two games share similar base logic: prefix search. Therefore, the idea is to utilize a prefix tree (Trie) to solve the games.
</p>
