from random import random, uniform
import sys

def pos(i, j):
    return i * n + j

def gen_mines(size):
    lim_inf = 0.125 * size 
    lim_sup = 0.5 * size
    return int(uniform(lim_inf, lim_sup))

def get_matrix(mines, size): #It is a vector, actually
    boxes = [False for x in range(size)]
    for mine in range(mines):
        pos = int(uniform(0, size))
        boxes[pos] = True
    return boxes;

def mines_around(index, matrix):
    i = -1
    around = 0
    while i < 2:
        j = -1
        while j < 2:
            next = index + i * n + j
            if next / n != (index / n + i):
                j += 1
                continue
            if 0 <= next < size and next != index and matrix[next] == True:
                around += 1
            j += 1
        i += 1
    return around

def get_boxes(matrix):
    index = 0
    boxes = []
    while index < size:
        mines = mines_around(index, matrix)
        box = Box(mines, matrix[index])
        boxes.append(box)
        index += 1
    return boxes

def open_around(index, boxes):
    i = -1
    to_open = []
    while i < 2:
        j = -1
        while j < 2:
            next = index + i * n + j
            if next / n != (index / n + i):
                j += 1
                continue
            if 0 <= next < size and next != index and boxes[next].open == False:
                to_open.append(next)
            j += 1
        i += 1
    return to_open

def open(pto, boxes):
    boxes[pto].open_box()
    to_open = []
    if boxes[pto].mines == 0:
        to_open = open_around(pto, boxes)
    for pto in to_open:
        boxes[pto].open_box()
    for pto in to_open:
        open(pto, boxes)

def imprimir(boxes):
    i = 0
    while i < size:
        box = boxes[i]
        if box.open == True:
            print box.mines, '\t',
        elif box.tagged == True:
            print '+\t',
        else:
            print '#\t',
        i += 1
        if i % n == 0:
            print ''


class Box:
    is_mine = False
    def __init__(self, mines, is_mine):
        self.mines = mines
        self.open = False
        self.is_mine = is_mine
        self.tagged = False
    def open_box(self):
        self.open = True
        if self.is_mine == True:
            print "Ya perdiste :("
            sys.exit(0)
    def tag_bomb(self):
        self.tagged = True
            #salir del programa

#Reading the size of the Minesweeper
print 'Dimensiones del buscaminas'
m = input('Filas: ')
n = input('Columnas: ')
size = m * n
#
mines = gen_mines(size)
matrix = get_matrix(mines, size)
boxes = get_boxes(matrix)
i = 0
while i < size:
    print matrix[i], ' ',
    i += 1
    if i % n == 0:
        print ''
while True:
    print '\n\nBuscaminas'
    imprimir(boxes)
    opc = raw_input("Abrir/Etiquetar [A/E]? ")
    print "Coordenadas(i, j)"
    i = input("i: ")
    j = input("j: ")
    pto = pos(i, j)
    if opc == "A":
        open(pto, boxes)
    elif opc == "E":
        boxes[pto].tag_bomb()