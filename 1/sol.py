import sys
import bisect

sums = []
cur_sum = 0
for line in sys.stdin:
    if line.strip():
        cur_sum += int(line)
    else:
        bisect.insort(sums, cur_sum)
        cur_sum = 0

print(sum(sums[-3:]))