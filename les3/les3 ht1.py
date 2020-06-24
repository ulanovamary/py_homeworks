def my_func(dig_1: int, dig_2: int)->int:
    try:
        result = int(dig_1)/int(dig_2)
    except ZeroDivisionError:
        result = 0
    return result


first = input('Введите первое число')
second = input('Введите второе число')
print(my_func(first, second))