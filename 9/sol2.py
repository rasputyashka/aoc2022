visited = set([(0, 0)])

SIZE = 10

visited.add((0, 0))
xs = {"R": 1, "L": -1, "U": 0, "D": 0}
ys = {"U": 1, "D": -1, "R": 0, "L": 0}


def get_abs_distances(x1, y1, x2, y2):
    return abs(x1 - x2), abs(y1 - y2)


snake = [[0, 0] for _ in range(SIZE)]

for line in open(0):
    line = line.strip()
    direction, times = line.split()
    times = int(times)

    for _ in range(times):
        snake[0][0] += xs[direction]
        snake[0][1] += ys[direction]
        for i in range(SIZE-1):
            cur_x, cur_y = snake[i]
            next_x, next_y = snake[i+1]
            dist_x, dist_y = abs(cur_x - next_x), abs(cur_y - next_y)

            if dist_x > 1 or dist_y > 1:

                next_y += 1 if cur_y - next_y > 0 else -1 if cur_y - next_y < 0 else 0
                next_x += 1 if cur_x - next_x > 0 else -1 if cur_x - next_x < 0 else 0

            snake[i+1] = [next_x, next_y]
            visited.add(tuple(snake[-1]))
print(len(visited))
