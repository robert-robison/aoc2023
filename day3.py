from collections import defaultdict
from aocd import get_data, submit

yr = 2023
day = 3

data = get_data(day=day, year=yr)
# data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""

data = data.splitlines()


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def get_idx(i1, i2, j):
    ir = range(i1 - 1, i2 + 2)
    return (
        [[ir[i], j - 1] for i in range(len(ir))]
        + [[ir[i], j + 1] for i in range(len(ir))]
        + [[i1 - 1, j]]
        + [[i2 + 1, j]]
    )


def check_for_symbol(i1, i2, j):
    all_idx = get_idx(i1, i2, j)
    # print(all_idx)
    # asdfad
    for i in range(len(all_idx)):
        try:
            val = data[all_idx[i][1]][all_idx[i][0]]
        except IndexError:
            continue
        if val == "*":
            return all_idx[i][1], all_idx[i][0]
    return -1, -1


def a(data):
    ans1 = 0
    for i, s in enumerate(data):
        j = 0
        while True:
            try:
                intval = isint(s[j])
            except IndexError:
                break
            if intval:
                ss = s[j]
                j_ = j + 1
                while True:
                    if isint(s[j_]):
                        ss += s[j_]
                        j_ += 1
                    else:
                        break
                    if len(s) == j_:
                        break
                val = int(ss)
                if check_for_symbol(j, j_ - 1, i):
                    # print(val)
                    ans1 += val
                j += len(ss)
            else:
                j += 1
    return ans1


gear_dict = defaultdict(list)


def b(data):
    for i, s in enumerate(data):
        j = 0
        while True:
            try:
                intval = isint(s[j])
            except IndexError:
                break
            if intval:
                ss = s[j]
                j_ = j + 1
                while True:
                    if isint(s[j_]):
                        ss += s[j_]
                        j_ += 1
                    else:
                        break
                    if len(s) == j_:
                        break
                val = int(ss)
                x, y = check_for_symbol(j, j_ - 1, i)
                gear_dict[f"{x}_{y}"].append(val)
                j += len(ss)
            else:
                j += 1
    res_items = [v for k, v in gear_dict.items() if len(v) == 2]
    return sum(item[0] * item[1] for item in res_items)


# ans1 = a(data)
# submit(ans1, part="a", day=day, year=yr)


ans2 = b(data)
print(ans2)
submit(ans2, part="b", day=day, year=yr)
