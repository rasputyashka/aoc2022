rows = 0
columns = 0
matrix = []
for line in open(0):
    rows += 1
    line = line.strip()
    matrix.append([int(x) for x in line])
else:
    columns = len(line)

max_score = 1

for row_idx, row in enumerate(matrix[1:-1], 1):
    for column_idx, cur_el in enumerate(row[1:-1], 1):

        see_left = 0
        see_right = 0
        see_above = 0
        see_below = 0

        for right in range(column_idx + 1, len(row)):
            if row[right] < cur_el:
                see_right += 1
            else:
                see_right += 1
                break

        for left in range(column_idx - 1, -1, -1):
            if row[left] < cur_el:
                see_left += 1
            else:
                see_left += 1
                break

        for above in range(row_idx - 1, -1, -1):
            if matrix[above][column_idx] < cur_el:
                see_above += 1
            else:
                see_above += 1
                break

        for below in range(row_idx + 1, len(matrix)):
            if matrix[below][column_idx] < cur_el:
                see_below += 1
            else:
                see_below += 1
                break

        cur_score = see_left * see_below * see_right * see_above
        max_score = max(max_score, cur_score)

# print("RES")
print(max_score)

