visited = set()

hx = hy = 0
tx = ty = 0
visited.add((0, 0))
xs = {"R": 1, "L": -1, "U": 0, "D": 0}
ys = {"U": 1, "D": -1, "R": 0, "L": 0}


def get_abs_distances(x1, y1, x2, y2):
    return abs(x1 - x2), abs(y1 - y2)


for line in open(0):
    line = line.strip()
    direction, times = line.split()
    times = int(times)
    
    for _ in range(times):
        cur_distances = get_abs_distances(hx, hy, tx, ty)
        new_x = hx + xs[direction]
        new_y = hy + ys[direction]
        new_distances = get_abs_distances(new_x, new_y, tx, ty)

        if sum(new_distances) == 3:
            tx = hx
            ty = hy

        elif sum(new_distances) == 2:
            if new_distances != (1, 1):
                tx = hx
                ty = hy

        hx = new_x
        hy = new_y
        visited.add((tx, ty))

print(len(visited))
