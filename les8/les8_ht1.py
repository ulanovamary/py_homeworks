'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
 год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
  месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
'''

class YearException (Exception):
    def __init__(self, text):
        self.text = text

class MonthException (Exception):
    def __init__(self, text):
        self.text = text

class DayException (Exception):
    def __init__(self, text):
        self.text = text


class Date:
    pass

    @classmethod
    def sep_date(cls, date:str):
        date_list = []
        for el in date.split('-'):
            if el != '-':
                date_list.append(int(el))
            #print(date_list)
        dd, mm, yyyy = date_list[0], date_list[1], date_list[2]
        #print(dd, mm, yyyy)
        return Date.valid(dd, mm, yyyy)

    @staticmethod
    def valid(dd, mm, yyyy):
        if dd <= 31 and dd >= 1:
            if mm <= 12 and mm >= 1:
                if yyyy <= 9999:# and len(yyyy) == 4:
                    return f'{dd}-{mm}-{yyyy}'
                raise YearException('Неверно введен год')
            raise MonthException('Неверно введен месяц')
        raise DayException('Неверно введен день')


a = Date
print(a.sep_date("12-12-2020"))



