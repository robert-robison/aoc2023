from aocd import get_data, submit

yr = 2023
day = 4

data = get_data(day=day, year=yr)
# data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
data = data.splitlines()


def a():
    ans1 = 0
    for i, s in enumerate(data):
        dd = s.split(": ")[1]
        l1 = [int(val) for val in dd.split(" | ")[0].split()]
        l2 = [int(val) for val in dd.split(" | ")[1].split()]
        val = len([ll for ll in l2 if ll in l1]) - 1
        if val >= 0:
            ans1 += 2**val
    return ans1


def score_card(s):
    dd = s.split(": ")[1]
    l1 = [int(val) for val in dd.split(" | ")[0].split()]
    l2 = [int(val) for val in dd.split(" | ")[1].split()]
    val = len([ll for ll in l2 if ll in l1])  # - 1
    return val


def b():
    ll = {k: 1 for k in range(len(data))}
    ans = 0
    for i, s in enumerate(data):
        val = score_card(s)
        ans += ll[i]
        for j in range(val):
            ll[i + j + 1] += ll[i]
    return ans


# ans1 = a()
# print(ans1)
# submit(ans1, part="a", day=day, year=yr)


ans2 = b()
print(ans2)
submit(ans2, part="b", day=day, year=yr)
