import dots, random
import numpy as np
import matplotlib.pyplot as plt

K = None
size = None

def classify(xns, yns, xks, yks):
    global K
    global size
    i = 0
    while i < size:
        pi = (xns[i], yns[i])
        pj = (xks[0], yks[0])
        min, j = dots.distance(pi, pj), 1
        while j < len(xks):
            pj = (xks[j], yks[j])
            dist = dots.distance(pi, pj)
            #print dist
            if(dist < min):
                min = dist
                K[i] = j
            j += 1
        i += 1

def sum_of(array, cond):
    global size
    sum, i = 0, 0
    length = 0
    while i < size:
        if K[i] == cond:
            sum += array[i]
            length += 1
        i += 1
    if length == 0: length = 1
    return sum, length

def get_class(array, cond):
    global size
    ran = range(size)
    return [array[i] for i in ran if K[i] == cond]

def change(KM):
    global K
    global size
    i, e = 0, 0.0
    while i < size:
        if K[i] != KM[i]: e += 1
        i += 1
    return e / size

def main():
    global K
    global size
    n, lim = 10000, 1000000
    k = 50
    xns = dots.generate(n, lim)
    yns = dots.generate(n, lim)
    xks = dots.generate(k, lim)
    yks = dots.generate(k, lim)
    size = len(xns)
    K = [-1 for x in range(size)]
    ####################################
    print xks, yks
    error = 1.0
    while error > 0.006:
        KM = K[:]
        classify(xns, yns, xks, yks) #Clasificaciones de cada n punto
        error = change(KM)
        print error
        i = 0
        while i < k:
            sx, lx = sum_of(xns, i)
            sy, ly = sum_of(yns, i)
            cx = sx / lx
            cy = sy / ly
            #Nuevo centroide
            xks[i] = cx
            yks[i] = cy
            i += 1

    print 'Graficando...'
    i = 0
    while i < k:
        x = get_class(xns, i)
        y = get_class(yns, i)
        plt.scatter(x, y)
        i += 1
    plt.scatter(xks, yks, marker='^', c='black')
    plt.show()

main()