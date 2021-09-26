import datetime

def logger(file_path):
    def time_func(function):
        def new_func(*args, **kwargs):
            start = datetime.datetime.now()
            func_name = function.__name__
            result = function(*args, **kwargs)
            with open(file_path, "a", encoding="utf-8") as file:
                file.write(f'Дата/время: {start}\n'
                          f'Имя функции: {func_name}\n'
                          f'Аргументы: {args, kwargs}\n'
                          f'Результат: {result}\n')
            return result
        return new_func
    return time_func

@logger('result_data.txt')
def date_function(a, b):
    return a + b
if __name__ == "__main__":
    date_function(10, 20)

