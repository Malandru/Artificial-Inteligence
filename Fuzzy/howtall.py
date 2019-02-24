from myreader import getInfo
from math import pi, atan

avg = 1.64

def is_tall(high):
    x = 16 * (high - avg)
    return atan(x) / pi + 0.5

fields, data = getInfo()
print fields, data

for row in data:
    print row[0], is_tall(row[1])