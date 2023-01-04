rows = 0
columns = 0
matrix = []
for line in open(0):
    rows += 1
    line = line.strip()
    matrix.append([int(x) for x in line])
else:
    columns = len(line)

visible = 2 * (columns + rows - 2)

for i, i_el in enumerate(matrix[1:-1], 1):
    for j, j_el in enumerate(i_el[1:-1], 1):
        current_element = j_el
        is_visible = False

        # row checking
        if not is_visible:
            for tree_before in matrix[i][:j]:
                if tree_before >= j_el:
                    break
            else:
                is_visible = True
        if not is_visible:
            for tree_after in matrix[i][j+1:]:
                if tree_after >= j_el:
                    break
            else:
                is_visible = True

        # column checking
        
        if not is_visible:
            for tree_before_idx in range(i):
                if matrix[tree_before_idx][j] >= j_el:
                    break
            else:
                is_visible = True
            
        if not is_visible:
            for tree_after_idx in range(i+1, rows):
                if matrix[tree_after_idx][j] >= j_el:
                    break
            else:
                is_visible = True
        if is_visible:
            visible += 1

print(visible)