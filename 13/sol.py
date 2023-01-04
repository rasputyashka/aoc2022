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


cnt = 1
ans = 0
for gp in open(0).read().strip().split("\n\n"):
    left, right = gp.split()
    left = ast.literal_eval(left)
    right = ast.literal_eval(right)
    if is_smaller(left, right):
        ans += cnt
    cnt += 1
print(ans)
