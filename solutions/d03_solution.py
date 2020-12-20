import os
import math

dirname = os.path.dirname(os.path.abspath(''))
filename = os.path.join(dirname,'inputs','d03_input.txt')

puzzle = open(filename,"r").read().splitlines()

def treecount(treemap, slope):
    trees = 0
    right,down = (0,0)
    while down < len(treemap):
        if treemap[down][right % len(treemap[0])] == '#':
            trees +=1
        right += slope[0]
        down += slope[1]
    return trees

p1slope = (3,1)
print(treecount(puzzle,p1slope))
p2slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
print(math.prod(treecount(puzzle,slope) for slope in p2slopes))