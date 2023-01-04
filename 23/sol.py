# flake8: noqa
from collections import deque

taken = set()
# is it possible to wrap it in a one line?
for r, rvalue in enumerate(open(0).read().splitlines()):
    for c, cvalue in enumerate(rvalue):
        if cvalue == "#":
            taken.add(c + r * 1j)
elves_count = len(taken)

check_pos = {
    -1j: [-1j - 1, -1j, -1j + 1],
    -1: [-1 - 1j, -1, -1 + 1j],
    1j: [1j - 1, 1j, 1j + 1],
    1: [1 - 1j, 1, 1 + 1j],
}

moves = deque([-1j, 1j, -1, 1])
positions = [-1 - 1j, -1j, -1j + 1, 1, 1 + 1j, 1j, 1j - 1, -1]

minx = miny = float("inf")
maxx = maxy = -float("inf")

for _ in range(
    10
):  # replace it with a number like 10000 if you wanna solve part 2 of the problem
    one_prop = set()
    two_prop = set()
    # round part 1
    # IG it's impossible to add the second part of the roud to the first one and vice versa because you must
    # determine whether only one elf has chosen the specified position
    for elf in taken:
        if not any(elf + pos in taken for pos in positions):
            continue
        for move in moves:
            if all(elf + shift not in taken for shift in check_pos[move]):
                moved = elf + move
                if moved in one_prop:
                    two_prop.add(moved)
                elif moved in two_prop:
                    pass
                else:
                    one_prop.add(moved)
                break
    # uncomment this if you wanna solve part 2 of the problem
    # if len(one_prop) == 0:
    #     print(_ + 1)
    #     exit(0)
    new_taken = taken.copy()

    # round part 2
    for elf in new_taken:
        if not any(elf + pos in new_taken for pos in positions):
            # again, elf is just standing
            continue
        for move in moves:
            if all(elf + shift not in new_taken for shift in check_pos[move]):
                moved = elf + move
                if moved not in two_prop:
                    taken.discard(elf)
                    taken.add(moved)
                break
    moves.append(moves.popleft())
minx = min(elf.real for elf in taken)
maxx = max(elf.real for elf in taken)
miny = min(elf.imag for elf in taken)
maxy = max(elf.imag for elf in taken)
print(int(maxx - minx + 1) * int(maxy - miny + 1) - elves_count)
