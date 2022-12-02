from dataclasses import dataclass
from functools import reduce
import uuid


test = False
file = 'data/task9test.txt' if test else 'data/task9.txt'

class Basin:
    nodes: list
    basinName: str

    def __init__(self):
        self.basinName=str(uuid.uuid4())
        self.nodes = list()

    def __repr__(self):
        return "Basin: {} Nodes:{}".format(self.basinName,self.nodes)

@dataclass
class Node:
    depth: int
    basin: Basin
    id: str

    def __init__(self, depth=9, basin=None):
        self.depth = depth
        self.basin = basin
        self.id = str(uuid.uuid4())

    def __repr__(self):
        lbasinName = self.basin.basinName if self.basin is not None else "None"
        return "Depth: {}\tBasin: {}".format(self.depth,lbasinName)

basins = []
with open(file) as f:
    depthmap = [[Node(int(x)) for x in list(y)] for y in f.read().splitlines()]
risk = 0

def getLeftNeighbor(node: Node):
    return getNeighbor(node,"LEFT")

def getRightNeighbor(node: Node):
    return getNeighbor(node,"RIGHT")

def getUpNeighbor(node: Node):
    return getNeighbor(node,"UP")

def getDownNeighbor(node: Node):
    return getNeighbor(node,"DOWN")

def getNeighbor(node: Node,direction):
    ymax = len(depthmap)-1
    xmax = len(depthmap[0])-1
    nodeCoords = [(i, line.index(node)) for i, line in enumerate(depthmap) if node in line][0]
    if nodeCoords[0] == ymax and direction=='DOWN':
        return Node(9)
    if nodeCoords[0] == 0 and direction=='UP':
        return Node(9)
    if nodeCoords[1] == xmax and direction=='RIGHT':
        return Node(9)
    if nodeCoords[1] == 0 and direction=='LEFT':
        return Node(9)
    if direction=='LEFT':
        return depthmap[nodeCoords[0]][nodeCoords[1]-1]
    elif direction=='RIGHT':
        return depthmap[nodeCoords[0]][nodeCoords[1]+1]
    elif direction=='UP':
        return depthmap[nodeCoords[0]-1][nodeCoords[1]]
    elif direction=='DOWN':
        return depthmap[nodeCoords[0]+1][nodeCoords[1]]

def checkBasin(node: Node):
    global basins

    #quit if max depth or if we have a basin
    if node.depth == 9 or node.basin is not None:
        return

    #get neighbors
    left = getLeftNeighbor(node)
    right = getRightNeighbor(node)
    up = getUpNeighbor(node)
    down = getDownNeighbor(node)

    #assign a basin
    if down.basin is None and up.basin is None and right.basin is None and left.basin is None:
        newBasin = Basin()
        newBasin.nodes.append(node)
        basins.append(newBasin)
        node.basin = newBasin
    elif down.basin is not None:
        down.basin.nodes.append(node)
        node.basin = down.basin
    elif up.basin is not None:
        up.basin.nodes.append(node)
        node.basin = up.basin
    elif left.basin is not None:
        left.basin.nodes.append(node)
        node.basin = left.basin
    elif right.basin is not None:
        right.basin.nodes.append(node)
        node.basin = right.basin
    
    #Check if surrounding nodes are part of basin
    if left.depth != 9 and left.basin is None:
        checkBasin(left)
    if right.depth != 9 and right.basin is None:
        checkBasin(right)
    if up.depth != 9 and up.basin is None:
        checkBasin(up)
    if down.depth != 9 and down.basin is None:
        checkBasin(down)

for y in range(len(depthmap)):
    for x in range(len(depthmap[0])):
        val = depthmap[y][x]
        checkBasin(val)

scores = []
for basin in basins:
    scores.append(len(basin.nodes))
top3 = sorted(scores, reverse=True)[:3]
print(top3)
final = reduce(lambda x, y: x*y, top3)
print(final)