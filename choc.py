# Conway's Game of Life
import copy
import random
import time

width = 60
height = 20

# Create a list of list for the cells:
next_cells = []
for x in range(width):
    column = []
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append("#")
        else:
            column.append(" ")
    next_cells.append(column)

while True:
    print("\n\n\n\n\n\n")
    current_cell = copy.deepcopy(next_cells)

    for y in range(width):
        for x in range(width):
            print(current_cell[x][y], end=' ')
        print()

    for x in range(width):
        for y in range(height):
            leftcoord = (x - 1) % width
            rightcoord = (x + 1) % width
            abovecoord = (y - 1) % height
            belowcoord = (y + 1) % height

        numNeighbors = 0
        if current_cell[leftcoord][abovecoord] == "#":
            numNeighbors += 1
        elif current_cell[x][abovecoord] == "#":
            numNeighbors += 1
        elif current_cell[rightcoord][abovecoord] == "#":
            numNeighbors += 1
        elif current_cell[leftcoord][y] == "#":
            numNeighbors += 1
        elif current_cell[rightcoord][y] == "#":
            numNeighbors += 1
        elif current_cell[leftcoord][belowcoord] == "#":
            numNeighbors += 1
        elif current_cell[x][belowcoord] == "#":
            numNeighbors += 1
        elif current_cell[rightcoord][belowcoord] == "#":
            numNeighbors += 1

        if current_cell[x][y] == "#" and (numNeighbors == 2 or numNeighbors == 3):
            next_cells[x][y] = "#"
        elif current_cell[x][y] == " " and numNeighbors == 3:
            numNeighbors[x][y] = "#"
        else:
            next_cells[x][y] = " "
    time.sleep(1)
