import sys

def pos(i, j):
    global n
    return i * n + j

def get(c, index):
    global n
    c.append(index / n)
    c.append(index % n)

def add_cand(cand, index):
    global n
    c = []
    get(c, index)
    i = c[0]
    j = c[1]
    for k in range(-2, 3):
        x = i + k
        if not(0 <= x < n) or k == 0:
            continue
        l = 2 / k #Para formar la L del caballo
        Y = [j + l, j - l]
        for y in Y: #y debe estar en la misma fila de index
            if 0 <= y < n and y / n == j / n:
                next = pos(x, y)
                if next != index:
                    cand.append(next)

def busca(pos_final, actuales, k):
    nuevos = []
    for p in actuales: #Posicion p
        if p == pos_final:
            print k, ' ',
            return
        add_cand(nuevos, p)
    k += 1
    busca(pos_final, nuevos, k)

n = input('Lado del ajedrez [n]: ')
print 'Posicion inicial'
i = input('Fila: ')
j = input('Columna: ')
index = pos(i, j)
#
for pos_final in range(n * n):
    if pos_final % n == 0:
        print ''
    busca(pos_final, [index], 0)