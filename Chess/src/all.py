def recorre(a, index, k):
    if k == fin:
        global s
        s += 1
        print 'Solucion', s
        imprimir(a)
    else:
        k += 1
        cand = []
        rutas(a, index, cand)
        for c in cand:
            a[c] = k
            recorre(a, c, k)
            a[c] = -1

def rutas(a, index, cand):
    c = []
    get(c, index)
    i = c[0]
    j = c[1]
    p = 0
    while p < MAXCAND:
        x = i + alfa[p / 2]
        y = j + beta[p]
        if 0 <= x < n and y / n == j / n:
            index = pos(x, y)
            if a[index] == -1:
                cand.append(index)
        p += 1

def get(c, index):
    c.append(index / n)
    c.append(index % n)

def pos(i, j):
    return i * n + j

def imprimir(a):
    fila = 0
    for p in a:
        if fila % n == 0:
            print ''
        print p, '\t',
        fila += 1

def init():
    i = input('Fila: ')
    j = input('Columna: ')
    return pos(i, j)

#VARIABLES GLOBALES A USAR
MAXCAND = 8
alfa = [-2, -1, 1, 2]
beta = [1, -1, 2, -2, 2, -2, 1, -1]
s = 0 #contador de soluciones
#----------------------
n = input('Lado del ajedrez [n]: ')
fin = n * n - 1
b = [-1 for x in range(n * n)]
print 'Posicion inicial'
inicial = init()
b[inicial] = 0
print 'Calculando...'
recorre(b, inicial, 0)