cnt = 1
ans = 0
reg_val = 1
step = 1

matrix = [[''*40] for _ in range(6)]

def solve(reg_val, cnt):
    if cnt in [20, 60, 100, 140, 180, 220]:
        return reg_val * cnt
    else:
        return 0

for line in open(0):
    data = line.split()
    if data[0] == "noop":
        cnt += 1
        ans += solve(reg_val, cnt)
    else:
        value = int(data[1])
        cnt += 1
        ans += solve(reg_val, cnt)
        reg_val += value
        cnt += 1
        ans += solve(reg_val, cnt)

print(ans)
