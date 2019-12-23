# SuDoKu-Generator
A simple Python program to generate a SuDoKu puzzle board.

The puzzle is created using backtracking. Around 1/3rd of backtracking overhead is reduced by filling the 3 diagonal 3x3 grids with numbers first, as they dont clash horizontally/vertically. The final SuDoKu puzzle is created by randomy revealing 30 cells from the completely filled grid.

## Example
Puzzle:

![](https://github.com/VaibhavSaini19/SuDoKu-Generator/blob/master/puzzle.png)

Solution:

![](https://github.com/VaibhavSaini19/SuDoKu-Generator/blob/master/solution.png)
