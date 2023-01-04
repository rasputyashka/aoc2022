# since i believe this is the most complicated problem, i'll try to explain its solution

from collections import deque


# let's store valve's value in valves and valve's tunnels in tunnels
valves = {}
tunnels = {}


for line in open(0).readlines():
    line = line.strip()
    valve = line[6:8]
    flow = int(line.split("; ")[0].split("=")[1])
    paths = line.split("to ")[1].split(" ", 1)[1].split(", ")
    valves[valve] = flow
    tunnels[valve] = paths


# we need it for our bitmask in future
# acc i think there's another solution that does not require
# to have a bitmask, but i need it for caching the paths
nonzero = []


# let's find out the distance between all nonzero nodes
dists = {}


for valve in valves:
    if valve != "AA" and valves[valve] == 0:
        # ignore all zero values (but we mustn't ignore AA)
        continue

    if valve != "AA":
        nonzero.append(valve)
    dists[valve] = {valve: 0, "AA": 0}
    v = {valve}  # we do not need to return back
    queue = deque([(0, valve)])
    while queue:
        d, cur_v = queue.popleft()
        for nei in tunnels[cur_v]:
            if nei in v:
                continue
            if valves[nei]:
                dists[valve][nei] = d + 1

            v.add(nei)
            queue.append((d + 1, nei))

    del dists[valve][valve]
    if valve != "AA":
        del dists[valve]["AA"]


# the most weird part of the solution
# now we just need to choose the best way for us - dfs (since we have the correct graph)
cache = {}

bits = {el: pos for pos, el in enumerate(nonzero)}


def solve(moves_left, cur_node, opened: int):
    # print(moves_left, cur_node, opened)
    if (moves_left, cur_node, opened) in cache:
        return cache[(moves_left, cur_node, opened)]
    maxval = 0
    for valve in dists[cur_node]:
        time_left = moves_left - dists[cur_node][valve] - 1
        bit = 1 << bits[valve]
        if opened & bit:
            continue
        if time_left <= 0:
            continue
        maxval = max(
            solve(time_left, valve, opened | bit) + valves[valve] * time_left,
            maxval,
        )
    cache[(moves_left, cur_node, opened)] = maxval
    return maxval


# i had to take a hint for that but nvm
# let's pretend that all vault are now opened
ans = 0

all_opened = (
    1 << len(nonzero)
) - 1  # 1 << 4 gives us '1' and four zeros if we substract one, then it will give us 1111

for x in range((all_opened + 1) // 2):
    ans = max(ans, solve(26, "AA", x) + solve(26, "AA", all_opened - x))

print(ans)
