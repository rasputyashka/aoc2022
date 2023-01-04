import ast


def is_smaller(left, right):
    if isinstance(left, int):
        if isinstance(right, int):
            if left == right:
                return None
            else:
                return left < right
        if isinstance(right, list):
            return is_smaller([left], right)
    if isinstance(left, list):
        if isinstance(right, int):
            return is_smaller(left, [right])
        if isinstance(right, list):
            for lft, rght in zip(left, right):
                res = is_smaller(lft, rght)
                if res is not None:
                    return res
            if len(left) == len(right):
                return None
            return len(left) < len(right)

    return left < right


class SortItem:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return is_smaller(self.value, other.value)

    def __repr__(self):
        return repr(self.value)


cnt = 1
ans = 0
dta = []
for gp in open(0).read().strip().split("\n\n"):
    left, right = gp.split()
    left = SortItem(ast.literal_eval(left))
    right = SortItem(ast.literal_eval(right))
    dta.extend([left, right])

a = SortItem([[2]])
b = SortItem([[6]])
dta.extend([a, b])
dta.sort()
print((dta.index(a) + 1) * (dta.index(b) + 1))
