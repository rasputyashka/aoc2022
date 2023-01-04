from __future__ import annotations

from dataclasses import dataclass

# the solution for the first part does not need the * 811589153 and for _ in range(10).


@dataclass
class Node:
    val: int
    next: Node = None
    prev: Node = None

    def __repr__(self):
        return str(self.val)


lst = [Node(int(val.strip()) * 811589153) for val in open(0)]
cp = lst[:]

lst[0].prev = lst[-1]
lst[-1].next = lst[0]
for pos, x in enumerate(lst[1:-1], 1):
    lst[pos - 1].next = x
    x.prev = lst[pos - 1]
    x.next = lst[pos + 1]
    lst[pos + 1].prev = x


for _ in range(10):
    for el in lst:
        if el.val == 0:
            zero = el
            continue
        value = el.val
        el.prev.next = el.next
        el.next.prev = el.prev
        tmp = el
        if value > 0:
            for _ in range(value % (len(lst) - 1)):
                prev_el = tmp.next
                tmp = prev_el

            el.prev = prev_el
            el.next = prev_el.next
            prev_el.next.prev = el
            prev_el.next = el

        else:
            for _ in range(abs(value) % (len(lst) - 1)):
                next_el = tmp.prev
                tmp = next_el
            el.next = next_el
            el.prev = next_el.prev
            next_el.prev.next = el
            next_el.prev = el

result = 0
cur = zero
for i in range(3):
    for j in range(1000):
        zero = zero.next
    result += zero.val

print(result)
