#OPenSAP Week 5 Unit 6 exercise
from sudoku import Sudoku

puzzle = Sudoku(3).difficulty(0.7)
print(puzzle.show())

solution = puzzle.solve()
print(solution.show())