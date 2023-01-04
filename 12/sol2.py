from collections import deque

# this shit is not working, probably because of ~ stuff i tried to do

data = open(0).read().splitlines()
matrix = [["~" for _ in range(len(data[0]) + 2)]]
for row, r_content in enumerate(data):
    rw = ["~"]
    for pos, char in enumerate(r_content):
        rw.append(char)
        if char == "S":
            start = row + 1, pos + 1
        if char == "E":
            end = row + 1, pos + 1
    rw.append("~")
    matrix.append(rw)
matrix.append(matrix[0])
matrix[start[0]][start[1]] = "a"
matrix[end[0]][end[1]] = "z"
paths = deque()
paths.append((1, end[0], end[1]))
visited = set()
while paths:
    cnt, y, x = paths.popleft()
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]:
        if (ny, nx) in visited:
            continue
        if nx == 0 or ny == 0 or nx == len(matrix[0]) or ny == len(matrix):
            continue
        if ord(matrix[ny][nx]) - ord(matrix[y][x]) < -1:
            continue
        if matrix[ny][nx] == "a":
            print(cnt)
            exit(0)
        visited.add((ny, nx))
        paths.append((cnt + 1, ny, nx))
