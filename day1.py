from aocd import get_data, submit

yr = 2023
day = 1

data = get_data(day=day, year=yr)

def _isint(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

def get_cal(s):
    val = 0
    for i in s:
        if _isint(i):
            val += 10 * int(i)
            break
    for i in reversed(s):
        if _isint(i):
            val += int(i)
            break
    return val

def get_calb(s, rev=False):
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    idx = range(len(s))
    if rev:
        idx = reversed(range(len(s)))
    for i in idx:
        for j, num in enumerate(nums):
            if s[i:(i+len(num))] == num:
                return j +1
        if _isint(s[i]):
            return int(s[i])    


# ans = sum(get_cal(val) for val in data.splitlines())
ansb = sum(10 * get_calb(val) for val in data.splitlines()) + sum(get_calb(val, rev=True) for val in data.splitlines())

# submit(ans, part="a", day=day, year=yr)
print(ansb)
submit(ansb, part="b", day=day, year=yr)

