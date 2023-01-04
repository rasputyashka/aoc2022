cnt = 1
reg_val = 1
step = 1

matrix = [["" for j in range(40)] for _ in range(6)]


def update(cnt, reg_val):
    cnt -= 1
    char = "."
    if cnt < 240:
        if cnt % 40 in range(reg_val - 1, reg_val + 2):
            char = "#"
        matrix[cnt // 40][cnt % 40] = char


for line in open(0):
    data = line.split()
    if data[0] == "noop":
        update(cnt, reg_val)
        cnt += 1
    else:
        update(cnt, reg_val)
        value = int(data[1])
        cnt += 1
        update(cnt, reg_val)
        cnt += 1
        reg_val += value

print(*["".join(row) for row in matrix], sep="\n")
print()