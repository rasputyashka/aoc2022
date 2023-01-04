line = input()
for pos, el in enumerate(line):
    if len(set(line[pos: pos+4])) == 4:
        print(pos + 4)
        break