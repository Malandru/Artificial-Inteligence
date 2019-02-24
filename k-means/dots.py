from random import randint

def generate(n, lim):
    return [randint(0, lim) for i in range(n)]

def distance(pt1, pt2):
    i = 0
    rad = 0
    while i < len(pt1):
        rad += (pt1[i] - pt2[i])**2
        i += 1
    return rad ** 0.5