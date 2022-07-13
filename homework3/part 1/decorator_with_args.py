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
            t = start_sleep_time
            stop = False
            for i in range(1,call_count+1):
                if t < border_sleep_time and i != 1:
                    t = start_sleep_time * (factor**i)
                if t >= border_sleep_time:
                    t = border_sleep_time
                    stop = True
                if i == call_count:
                    stop = True
                time.sleep(t)
                val = func(*args, **kwargs)
                print(f'Запуск номер {i}. Ожидание: {t} секунд. Результат декорируемой функций = {val}.')    
                if stop:
                    print('Конец Работы')
                    break
        return wrapper
    return my_decorator

@decorator_with_args(8, 1, 2, 100)
def func():
    return 'func_result'

if __name__ == '__main__':
    func()