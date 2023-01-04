# the idiea is to fill up the busy set which shows currently busy ceils (stone or sand)
busy = set()
bottom = 0

data = open(0).read().splitlines()
for line in data:
    pairs = line.split(" -> ")
    real_pairs = [list(map(int, el.split(","))) for el in pairs]
    for f_idx in range(len(real_pairs) - 1):
        x1, y1 = real_pairs[f_idx]
        x2, y2 = real_pairs[f_idx + 1]
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])

        for b_x in range(x1, x2 + 1):
            for b_y in range(y1, y2 + 1):
                busy.add((b_y, b_x))
                bottom = max(bottom, b_y + 1)  # the deeper - the greater b_y

bottom += 1
cnt = 1

while 1:
    x = 500
    y = 0
    while 1:
        if y == bottom:
            busy.add((y, x))
            break
        if (y + 1, x) not in busy:
            y += 1
            continue
        if (y + 1, x - 1) not in busy:
            y += 1
            x -= 1
            continue
        if (y + 1, x + 1) not in busy:
            y += 1
            x += 1
            continue
        if y == 0 and x == 500:
            print(cnt)
            exit(0)
        busy.add((y, x))
        cnt += 1
        break
