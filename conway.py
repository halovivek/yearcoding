# Conway game of life
import random, time, copy

WIDTH = 60
HEIGHT = 20

# CREATE A LIST FOR THE DETAILS

nextCells = []
for x in range(WIDTH):
    column = []  # create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#')  # add a living cell
        else:
            column.append('')  # add a dead cell
    nextCells.append(column)  # nextcell in a list of columns

while True:  # main loop program
    print('\n\n\n\n\n')  # separate each steps with newline
    currentCells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x], [y], end='')
        print()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y - 1) % HEIGHT

            numNeighbors = 0
            if currentCells[rightCoord][rightCoord] == '#':
                numNeighbors += 1
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1  # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1  # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1  # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1  # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1  # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1  # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1  # Bottom-right neighbor is alive.

            if currentCells[x][y] == '#' and (numNeighbors == 2 or
                                              numNeighbors == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1)  # Add a 1-second pause to reduce flickering.
