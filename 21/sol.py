import operator


a = []
nums = {}
exprs = {}
operator_m = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
}

for line in open(0):
    line = line.strip()
    name, rest = line.split(": ")
    if rest.isdigit():
        exprs[name] = int(rest)
        nums[name] = int(rest)
    else:
        exprs[name] = rest.split()


def get_number(name):
    if name in nums:
        return nums[name]
    left, op, right = exprs[name]
    left_n = get_number(left)
    nums[left] = left_n
    right_n = get_number(right)
    nums[right] = right_n
    op = operator_m[op]
    return op(left_n, right_n)


print(int(get_number("root")))
