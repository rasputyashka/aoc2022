# flake8: noqa

import re

pattern = re.compile("(\d+)(\w)?")
grid = []
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
    """add some padding to the end of each line of the grid"""
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


while ic < len(instructions):
    instr = instructions[ic]
    for _ in range(instr[0]):

        current_direction_row = direction_row
        current_direction_column = direction_column
        pr = r + direction_row
        pc = c + direction_column

        # see https://www.reddit.com/r/adventofcode/comments/zszb0l/2022_day_22_part_2_hey_if_it_works_it_works/

        if direction_row == -1:  # if going up
            if 50 <= pc < 100 and pr < 0:  # from 1 to 6
                direction_row, direction_column = 0, 1
                pr, pc = pc + 100, 0

            elif 100 <= pc < 150 and pr < 0:  # from 2 to 6
                pr, pc = 199, pc - 100

            elif 0 <= pc < 50 and pr == 99:  # from 5 to 3
                direction_row, direction_column = 0, 1
                pr, pc = pc + 50, 50
            # else:
            # print("ERROR 1")
        elif direction_row == 1:
            if 0 <= pc < 50 and pr >= 200:  # from 6 to 2
                pr, pc = 0, pc + 100

            elif 100 <= pc < 150 and pr == 50:  # from 2 to 3
                direction_row, direction_column = 0, -1
                pr, pc = pc - 50, 99

            elif 50 <= pc < 100 and pr == 150:  # from 4 to 6
                direction_row, direction_column = 0, -1
                pr, pc = pc + 100, 49
            # else:
            # print("ERROR 2")
        elif direction_column == -1:
            if 0 <= pr < 50 and pc == 49:  # from 1 to 5
                direction_column = 1
                pr, pc = 149 - pr, 0
            elif 50 <= pr < 100 and pc == 49:  # from 3 to 5
                direction_row, direction_column = 1, 0
                pr, pc = 100, pr - 50
            elif 100 <= pr < 150 and pc < 0:  # from 5 to 1
                direction_column = 1
                pr, pc = 149 - pr, 50
            elif 150 <= pr < 200 and pc < 0:  # from 6 to 1
                direction_row, direction_column = 1, 0
                pr, pc = 0, pr - 100
            # else:
            # print("ERROR 3")
        elif direction_column == 1:
            if 0 <= pr < 50 and pc >= 150:  # from 2 to 4
                direction_column = -1
                pr, pc = 149 - pr, 99
            elif 50 <= pr < 100 and pc == 100:  # from 3 to 2
                direction_row, direction_column = -1, 0
                pr, pc = 49, pr + 50
            elif 100 <= pr < 150 and pc == 100:  # from 4 to
                direction_column = -1
                pr, pc = 149 - pr, 149

            elif 150 <= pr < 200 and pc == 50:
                direction_row, direction_column = -1, 0
                pr, pc = 149, pr - 100

        # moving
        if grid[pr][pc] == "#":
            direction_row = current_direction_row
            direction_column = current_direction_column
            break
        r = pr
        c = pc
    ic += 1
    direction = instr[1]
    if direction == "R":
        direction_row, direction_column = direction_column, -direction_row
    elif direction == "L":
        direction_row, direction_column = -direction_column, direction_row
    # print(direction_row, direction_column)


if direction_row == 0:
    if direction_column == 1:  # input sample helped with filling this thing
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
