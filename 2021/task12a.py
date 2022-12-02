import numpy

test = False
file = 'data/12t.txt' if test else 'data/12.txt'

with open(file) as f:
    octipi = numpy.array([[int(x) for x in list(y)] for y in f.read().splitlines()])

tree traversal