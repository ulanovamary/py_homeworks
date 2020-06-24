n = int(input('Введите любое целое положительное число'))
maximum= n%10
n = n//10
while n > 0:
    if n%10 > maximum:
        maximum = n%10
    n = n//10
print(maximum)