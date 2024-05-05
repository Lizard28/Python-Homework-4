def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Функция {func.__name__} была вызвана с позиционными аргументами: {args} и именованными аргументами: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@decorator
def fibanachi(n):
    if n == 0:
        print('Пустое множество')
    x, y = 1, 1
    for i in range(n):
        yield x 
        x, y = y, x + y

n = int(input("Введите количество чисел Фибоначчи: "))

for i in fibanachi(n):
    print(i)