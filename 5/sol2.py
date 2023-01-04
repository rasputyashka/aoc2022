# flake8: noqa

from collections import deque, defaultdict
import sys
import string

mapping = defaultdict(deque)
stack_ended = False
for line in sys.stdin:
    if not line.strip():
        stack_ended = True
        continue  # опять делитель блоков и команд
    if not stack_ended:
        idx = 1
        for char in line:
            idx += 1
            if char in string.ascii_letters:
                mapping[(idx+1)//4].append(char)
    else:
        amount, from_, to = [int(char) for char in line.split() if char.isdigit()]
        buffer = deque()  # буффер реализует возможность сохранять позицию
        
        for _ in range(amount):
            buffer.append(mapping[from_].popleft())
        for _ in range(amount):
            mapping[to].appendleft(buffer.pop())

print(*[mapping[queue][0] for queue in sorted(mapping)], sep='')