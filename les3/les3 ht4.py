def my_func(x:int, y:int):
    if x < 0:
        print(int(input('Введите действительное положительное число')))
    else:
        if y > 0:
            print(int(input('Введите целое отрицательное число')))
        else:
            pass
    i = abs(y)
    print('Введите целое отрицательное число')
    result = pow(x, y) #x ** y
    return result

x = 10
y = -2

print(my_func(x, y))

'''
def my_func(x, y):
    if x < 0:
        print(int(input('Введите действительное положительное число')))
    else:
        if y > 0:
            print(int(input('Введите целое отрицательное число')))
    i = abs(y)
    result = 1
    while i >= 1:
        result = 1 / (result * x)
        i -= 1
    return result


x = 10
y = -2
print(my_func(x, y))
'''