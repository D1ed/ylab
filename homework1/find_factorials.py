def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans


def count_find_num(primesL, limit):
    count = 0
    end = []
    end_i = 1
    for n in reversed(range(limit+1)):
        if list(set(Factor(n))) == primesL:
            count += 1
            end += [Factor(n)]

    if len(end):
        for _, n in enumerate(end[0]):
            end_i *= n
        return [count, end_i]
    else:
        return []


primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
