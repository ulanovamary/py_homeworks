'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного
результата.
'''

class ComplexDigit:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        sign = '+' if self.imag >= 0 else ''
        return '{}{}{}i'.format(self.real, sign, self.imag)


class Calculator:
    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        print(ComplexDigit(real, imag))

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.imag * other.real + self.real * other.imag
        print(ComplexDigit(real, imag))


calc = Calculator
a = ComplexDigit(1, 3)
b = ComplexDigit(2, -4)
calc.__add__(a, b)
calc.__mul__(a, b)

