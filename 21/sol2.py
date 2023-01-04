import operator
from collections import deque
import sympy

stack = deque()
exprs = {}
nums = {}
root_l = None
root_r = None


operator_m = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

reversed_ops = {
    "+": operator.sub,
    "-": operator.add,
    "*": operator.truediv,
    "/": operator.mul,
}

for line in open(0):
    line = line.strip()
    name, rest = line.split(": ")
    if name == "humn":
        nums[name] = None
    if name == "root":
        left, _, right = rest.split()
        root_l = left
        root_r = right
        continue
    if rest.isdigit():
        exprs[name] = int(rest)
        nums[name] = int(rest)
    else:
        exprs[name] = rest.split()


def get_number(name):
    if name in nums:
        return nums[name]
    if name == "humn":
        return None
    left, op, right = exprs[name]
    stack.append((name, left, op, right))
    left_n = get_number(left)
    right_n = get_number(right)
    if left_n is not None and right_n is not None:
        nums[left] = left_n
        nums[right] = right_n
        op = operator_m[op]
        return op(left_n, right_n)


try:
    number = get_number(root_r)
except:
    number = None
    pass
if number is not None:
    stack.clear()
    try:
        left_res = get_number(root_l)
    except:
        pass
    real_stack = stack.copy()
    to_find = root_l
    found = root_r

else:
    real_stack = stack.copy()
    stack.clear()
    try:
        number = get_number(root_l)
    except:
        pass
    to_find = root_r
    found = root_l


del nums["humn"]
nums[found] = number

s_ops = {"+": "-", "-": "+", "/": "*", "*": "/"}

# while real_stack:
#     name, left, op, right = real_stack.popleft()
#     if name in nums:
#         if left in nums:
#             nums[right] = s_ops[op](name, left)
#         elif right in nums:
#             nums[left] = s_ops[op](name, right)
# # print(real_stack)


# i've lost my original solution, but I used sympy there. Acc i'm kinda close to solve via this code, but i don't like it already
