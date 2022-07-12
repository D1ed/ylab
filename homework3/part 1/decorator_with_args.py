def decorator_with_args(call_count, start_sleep_time, factor, border_sleep_time):
    '''А decorator to re-execute the decorated function after some time.
     
    Keyword arguments:
    call_count: int, count of repeat function
    start_sleep_time: int, start time of repeat
    factor: int, a naive exponential growth of the repeat time
    border_sleep_time: int, end time of repeat
    '''
    import time
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print('Начало работы')
            t = 0
            for i in range(1,call_count+1):
                if t < border_sleep_time:
                    t = start_sleep_time * (factor**i)
                    val = func(*args, **kwargs)
                elif t >= border_sleep_time:
                    t = border_sleep_time
                    print('Конец Работы')
                    break
                elif i == call_count:
                    print('Конец Работы')
                    break
                time.sleep(t)
                print(f'Запуск номер {i}. Ожидание: {t} секунд. Результат декорируемой функций = {val}.')
                
        return wrapper
    return my_decorator

@decorator_with_args(5, 1, 2, 100)
def func():
    return 'func_result'

if __name__ == '__main__':
    func()