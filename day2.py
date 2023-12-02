from aocd import get_data, submit

yr = 2023
day = 2

data = get_data(day=day, year=yr)


def a(s):
    lookup = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    for ss in s.split(": ")[1].split("; "):
        for cub in ss.split(", "):
            val, color = cub.split()
            if int(val) > lookup[color]:
                return 0
    return int(s.split(":")[0].split()[1])


def b(s):
    mins = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for ss in s.split(": ")[1].split("; "):
        for cub in ss.split(", "):
            val, color = cub.split()
            mins[color] = max(mins[color], int(val))
    return mins["red"] * mins["green"] * mins["blue"]

ans1 = sum(a(s) for s in data.splitlines())


submit(ans1, part="a", day=day, year=yr)


ans2 = sum(b(s) for s in data.splitlines())
print(ans2)
submit(ans2, part="b", day=day, year=yr)
