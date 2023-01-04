import sys

def fight(a, b):
    maps = {"X": "A", "Y": "B", "Z": "C"}
    win = {"A": "scissors", "B": "rock", "C": "paper"}
    loose = {"A": "paper", "B": "scissors", "C": "rock"}
    draw = {"A": "rock", "B": "paper", "C": "scissors"}
    b = maps[b]
    if b == 'C':
        return loose[a]
    if b == 'B':
        return draw[a]
    return win[a]


score = 0
for line in sys.stdin:
    a, b = line.split()
    results = {"X": 0, "Y": 3, "Z": 6}
    price = {"rock": 1, "paper": 2, 'scissors': 3}
    res = fight(a, b)
    # print(results[b], price[res])
    score += results[b] + price[res]

print(score)