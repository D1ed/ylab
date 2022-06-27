def count_find_num(primesL, limit):
    if multiply_all_primesL(primesL) > limit:
        return []
    res = list()
    res.append(multiply_all_primesL(primesL))
    for i in primesL:
        for value in res:
            value *= i
            while value <= limit and value not in res:
                res.append(value)
                value *= i
    end = max(res)
    count = len(res)
    return [count, end]

def multiply_all_primesL(s):
    ended_prime = 1
    for i in s:
        ended_prime *= i
    return ended_prime

primesL = [2, 3]
limit = 200
assert count_find_num(primesL, limit) == [13, 192]
print(count_find_num(primesL, limit))

primesL = [2, 5]
limit = 200
assert count_find_num(primesL, limit) == [8, 200]
print(count_find_num(primesL, limit))

primesL = [2, 3, 5]
limit = 500
assert count_find_num(primesL, limit) == [12, 480]
print(count_find_num(primesL, limit))

primesL = [2,5,7]
limit = 500
assert count_find_num(primesL, limit) == [5, 490]
print(count_find_num(primesL, limit))

primesL = [3,5,7]
limit = 500
assert count_find_num(primesL, limit) == [2, 315]
print(count_find_num(primesL, limit))

primesL = [2, 3, 5]
limit = 1000
assert count_find_num(primesL, limit) == [19, 960]
print(count_find_num(primesL, limit))

primesL = [2, 3, 47]
limit = 200
assert count_find_num(primesL, limit) == []
print(count_find_num(primesL, limit))

primesL = [2, 5, 23, 61]
limit = 1063585
assert count_find_num(primesL, limit) ==  [16, 897920]
print(count_find_num(primesL, limit))

primesL = [19, 29, 61]
limit = 2571423
assert count_find_num(primesL, limit) ==  [4, 2050271]
print(count_find_num(primesL, limit))
