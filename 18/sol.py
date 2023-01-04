from collections import defaultdict

mid_edge_points = defaultdict(int)

shifts_to_mid = [
    (0, 0, 0.5),
    (0, 0.5, 0),
    (0.5, 0, 0),
    (0, 0, -0.5),
    (0, -0.5, 0),
    (-0.5, 0, 0),
]

cnt = 0
for line in open(0).read().splitlines():
    cnt += 1
    x, y, z = data = [int(v) for v in line.split(",")]
    for sx, sy, sz in shifts_to_mid:
        edge_point = (sx + x, sy + y, sz + z)
        if edge_point in mid_edge_points:
            mid_edge_points[edge_point] += 1
        else:
            mid_edge_points[edge_point] = 1

print(mid_edge_points)
