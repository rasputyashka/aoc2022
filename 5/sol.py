# flake8: noqa

from collections import deque, defaultdict
import sys
import string

mapping = defaultdict(deque)
stack_ended = False
for line in sys.stdin:
    if not line.strip():
        stack_ended = True
        continue  # скипаем, если пробел (он там делит блоки от команд)
    if not stack_ended:
        idx = 1
        for char in line:
            idx += 1
            if char in string.ascii_letters:
                mapping[(idx+1)//4].append(char)
    else:
        amount, from_, to = [int(char) for char in line.split() if char.isdigit()]
        for _ in range(amount):
            el = mapping[from_].popleft()
            mapping[to].appendleft(el)

# тупо взять первый элемент из каждого блока
print(*[mapping[queue][0] for queue in sorted(mapping)], sep='')