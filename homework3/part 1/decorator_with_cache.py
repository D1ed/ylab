def my_decorator(func):
    '''Decorating a given function with cache.'''
    cache = {}
    def wrapper(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in cache:
            cache[cache_key] = func(*args, **kwargs)
        return cache[cache_key]
    return wrapper

@my_decorator
def multiplier(number: int):
    return number * 2

if __name__ == '__main__':
    print(multiplier(7))
    print(multiplier(10))
    print(multiplier(7))
    print(multiplier(9999999999999999))