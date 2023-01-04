line = input()
shift = 14
for pos, el in enumerate(line):
    if len(set(line[pos: pos+14])) == 14:
        print(pos + 14)
        break
