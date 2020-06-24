revenue = int(input('Введите выручку фирмы'))
costs = int(input('Введите издержки фирмы'))


if revenue > costs:
    print('Прибыль')
    profit = revenue - costs
    profitability = profit / revenue
    people = int(input('Введите численность сотрудников фирмы'))
    profit_per_person = profit/people
    print('Прибыль фирмы в расчете на сотрудника составляет : {}'.format(profit_per_person))
else:
    print('Убыток')
