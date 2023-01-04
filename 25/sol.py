from collections import deque

t = 0
for line in open(0).read().splitlines():
    ct = 0
    for pos, c in enumerate(line):
        if c == "=":
            c = -2
        elif c == "-":
            c = -1
        else:
            c = int(c)
        # print(pos, c)
        ct += c * 5 ** (len(line) - 1 - pos)
    t += ct


s = deque()
used = False
add = 0
while t > 0:
    c = t % 5
    t //= 5
    if c not in [3, 4]:
        c = add + c
    if c == 4:
        c = "-"
        t += 1
    if c == 3:
        c = "="
        t += 1

    # print(t)
    s.appendleft(c)
    if t == 0:
        if add:
            s.appendleft(add)
print("".join(map(str, s)))
