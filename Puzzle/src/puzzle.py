# Puzzle de dimension n*n
import backtrack

def read(matrix, size):
    for i in range(size):
        x = input()
        matrix.append(x)

n = input('Dimension de la matriz [n]: ')
size = n
matrix = []
read(matrix, size)
print backtrack.is_solution(matrix, n)