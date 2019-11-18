from pee2_e4 import *

prob_puzzle = PuzzleN()

print("Estado Inicial:",prob_puzzle.initial)
print('A dimensao é de:',prob_puzzle.d)
print("O objectivo é ",prob_puzzle.goal)
print()

prob_puzzle.display(prob_puzzle.initial)
e1 = prob_puzzle.initial
a1 = prob_puzzle.actions(e1)
print(a1)
e2 = prob_puzzle.result(e1, a1[0])

prob_puzzle.display(e2)
a2 = prob_puzzle.actions(e2)
print(a2)
e3 = prob_puzzle.result(e2, a2[0])

prob_puzzle.display(e3)
a3 = prob_puzzle.actions(e3)
print(a3)
e4 = prob_puzzle.result(e3, a3[0])

prob_puzzle.display(e4)
