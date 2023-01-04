# flake8: noqa

blocked = {x - 1j for x in range(7)}

pattern = [1 if x == ">" else -1 for x in input()]
pi = -1

blocks = [
    [0, 1, 2, 3],
    [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
    [0, 1, 2, 2 + 1j, 2 + 2j],
    [0, 1j, 2j, 3j],
    [0, 1, 1j, 1 + 1j],
]


height = 0
a = []
for i in range(2022):
    cur_block = {x + 2 + (height + 3) * 1j for x in blocks[i % len(blocks)]}
    # print(f"start block: {cur_block}")
    while 1:
        pi = (pi + 1) % len(pattern)
        moved_block = {x + pattern[pi] for x in cur_block}

        if (
            all([0 <= x.real < 7 for x in moved_block])
            and not moved_block & blocked
        ):
            cur_block = moved_block

        # go down
        moved_block = {x - 1j for x in cur_block}

        # hits the ground, right position now
        if moved_block & blocked:
            tmp = height
            blocked |= cur_block
            height = max(x.imag for x in blocked) + 1
            a.append(int(height - tmp))
            break
        cur_block = moved_block


# print(a)
print(int(height))
