# flake8: noqa

import re

pattern = re.compile("(\d+)(\w)?")

grid = []

moves = []
next_sequence = False
for r, line in enumerate(open(0)):
    line = line[:-1]  # ig rstrip won't work because '. # ' is possible
    if not line:
        next_sequence = True
    if next_sequence:
        instructions = line
    else:
        if r == 0:
            for c, el in enumerate(line):
                if el == ".":
                    start = c
                    break
        grid.append(line)


def normalise_grid(grid):
    """add some paddint to the end of each line of the grid"""
    maxlen = len(grid[0])
    for row in grid[1:]:
        if len(row) > maxlen:
            maxlen = len(row)
    grid = [row + " " * (maxlen - len(row)) for row in grid]
    return grid


grid = normalise_grid(grid)


instructions = list(
    map(lambda x: [int(x[0]), x[1]], re.findall(pattern, instructions))
)


direction_row = 0
direction_column = 1
ic = 0
c = start
r = 0

# print(instructions)
while ic < len(instructions):
    instr = instructions[ic]
    for _ in range(instr[0]):
        # memorize the last position if the next "wrapped" object is a block
        pr, pc = r, c
        # like try like go down\up riht\left while you don't heat # or .
        while 1:
            pr = (pr + direction_row) % len(grid)
            pc = (pc + direction_column) % len(grid[0])
            if grid[pr][pc] != " ":
                break
        if grid[pr][pc] == "#":
            break
        r, c = pr, pc
    direction = instr[1]
    if direction == "R":
        direction_row, direction_column = direction_column, -direction_row
    elif direction == "L":
        direction_row, direction_column = -direction_column, direction_row
    ic += 1
    # print(direction_row, direction_column)


print(r, c)
print(direction_row, direction_column)

if direction_row == 0:
    if direction_column == 1:
        res_dir = 0
    else:
        res_dir = 2
else:
    if direction_row == -1:
        res_dir = 3
    else:
        res_dir = 1

r += 1
c += 1


print(1000 * r + 4 * c + res_dir)
