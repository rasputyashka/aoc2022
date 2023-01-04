# flake8: noqa

import re

number_pattern = re.compile(r"\d+")


def solve(remtime, cache, balance, workers):
    if remtime == 0:
        return workers[-1]
    if (remtime, balance, workers) in cache:
        return cache[(remtime, tuple(balance), tuple(workers))]

    cache[x] = maxval
    return maxval

t = 0
brint = []
for pos, line in enumerate(open(0), 1):
    spent = [0, 0, 0]
    print(repr(line))
    line = line.strip()

    for x 

    t += solve(24, brint, spent, {}, [0, 0, 0, 0], [1, 0, 0, 0]) * pos
