grid = open(0).read().splitlines()
dx = {">": 0, "<": 0, "v": 1, "^": -1}
dy = {">": 1, "<": -1, "v": 0, "^": 0}

ROWS, COLUMNS = len(grid), len(grid[0])
cur = {(0, 1, 0)}
taken = []
for r, el in enumerate(grid):
    for c, char in enumerate(el):
        if grid[r][c] in dx:
            taken.append((r, c, grid[r][c]))

tm = 0
while (ROWS - 1, COLUMNS - 2, 2) not in cur:
    tm += 1
    s = set()
    nxt = []
    for r, c, d in taken:
        nr, nc = r + dx[d], c + dy[d]
        if nr == 0:
            nr = ROWS - 2
        elif nr == ROWS - 1:
            nr = 1
        elif nc == 0:
            nc = COLUMNS - 2
        elif nc == COLUMNS - 1:
            nc = 1
        s.add((nr, nc))
        nxt.append((nr, nc, d))
    taken = nxt[:]
    z = set()
    for r, c, k in cur:
        for mr, mc in [(r, c), (r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if (
                (mr, mc) not in s
                and 0 <= mr < ROWS
                and 0 <= mc < COLUMNS
                and grid[mr][mc] != "#"
            ):
                z.add(
                    (
                        mr,
                        mc,
                        k
                        + (
                            ((k, mr, mc) == (0, ROWS - 1, COLUMNS - 2))
                            or ((k, mr, mc) == (1, 0, 1))
                        ),
                    )
                )
    cur = z

print(tm)
