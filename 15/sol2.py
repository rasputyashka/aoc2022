import re

max_num = 4000000

number_pattern = re.compile(r"-?\d+")

data = [[int(x) for x in re.findall(number_pattern, line)] for line in open(0)]
for ROW_NUM in range(max_num + 1):
    # print(ROW_NUM)
    intervals = []
    for (sx, sy, bx, by) in data:
        distance = abs(sx - bx) + abs(sy - by)
        steps_left = distance - abs(ROW_NUM - sy)
        if steps_left < 0:
            continue
        intervals.append([sx - steps_left, sx + steps_left])
    intervals.sort()
    res = []
    res_int = intervals[0]
    for (bl, br) in intervals:
        if bl <= res_int[1] + 1:
            res_int[1] = max(res_int[1], br)
        else:
            res.append(res_int)
            res_int = [bl, br]
    else:
        res.append(res_int)
    if len(res) == 2:
        print(ROW_NUM + (res[1][0] - 1) * 4000000)
        break
