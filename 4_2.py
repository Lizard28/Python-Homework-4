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
