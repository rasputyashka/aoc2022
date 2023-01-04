import sys
cnt = 0
for line in sys.stdin:
    left, right = line.split(',')
    left_l, left_r = [int(x) for x in left.split('-')]
    right_l, right_r = [int(x) for x in right.split('-')]
    if (right_l <= left_l <= right_r) or (right_l <= left_r <= right_r):
        cnt += 1
    elif (left_l <= right_l <= left_r) or (left_l <= right_r <= left_r):
        cnt += 1
print(cnt)