import numpy

coords = []
grid = numpy.zeros((1000, 1000))
with open('task5.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        coords.append(line.split(' -> '))

for coord in coords:
    coord1 = coord[0].split(',')
    coord2 = coord[1].split(',')
    coord1_x = int(coord1[0])
    coord1_y = int(coord1[1])
    coord2_x = int(coord2[0])
    coord2_y = int(coord2[1])
    if coord1[0] == coord2[0]:
        x = coord1_x
        large_y = coord1_y if coord2_y <= coord1_y else coord2_y
        small_y = coord1_y if coord2_y >= coord1_y else coord2_y
        for y in range(small_y,large_y+1):
            grid[x][y] += 1
    elif coord1[1] == coord2[1]:
        y = coord1_y
        large_x = coord1_x if coord2_x  <= coord1_x else coord2_x 
        small_x = coord1_x if coord2_x  >= coord1_x else coord2_x 
        for x in range(small_x,large_x+1):
            grid[x][y] += 1
    else:
        slope = (coord1_y-coord2_y)/(coord1_x-coord2_x )
        intercept = coord1_y-slope*coord1_x
        large_x = coord1_x if coord2_x  <= coord1_x else coord2_x 
        small_x = coord1_x if coord2_x  >= coord1_x else coord2_x 
        for x in range(small_x,large_x+1):
            large_y = coord1_y if coord2_y <= coord1_y else coord2_y
            small_y = coord1_y if coord2_y >= coord1_y else coord2_y
            for y in range(small_y,large_y+1):
                if y == slope*x+intercept:
                    grid[x][y] += 1


print(grid)
print((grid >= 2).sum())