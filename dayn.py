from aocd import get_data, submit

yr = 2023
day = 1

data = get_data(day=day, year=yr)


def a(s):
    pass


ans1 = sum(a(s) for s in data.splitlines())

submit(ans1, part="a", day=day, year=yr)


# ans2 = sum(b(s) for s in data.splitlines())
# submit(ans2, part="b", day=day, year=yr)
