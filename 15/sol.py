import re

number_pattern = re.compile(r"-?\d+")
occupied = set()
beacon_met = set()

row = 10

intervals = []

for line in open(0):
    sx, sy, bx, by = [int(x) for x in re.findall(number_pattern, line)]
    distance = abs(sx - bx) + abs(sy - by)
    print(distance)
    steps_left = distance - abs(row - sy)
    if by == row:
        beacon_met.add(bx)
    if steps_left < 0:
        continue
    # print([sx - steps_left, sx + steps_left])
    intervals.append([sx - steps_left, sx + steps_left])

print(intervals)
intervals.sort()
res = []
res_int = intervals[0]
for (bl, br) in intervals:
    if bl <= res_int[1] + 1:
        res_int[1] = br
    else:
        res.append(res_int)
        res_int = [bl, br]
else:
    res.append(res_int)

print(res)
if len(res) != 1:
    print(
        2 + (res[0][1] + res[0][0]) + (res[1][1] - res[1][0]) - len(beacon_met)
    )
else:
    print(res[0][1] - res[0][0])
