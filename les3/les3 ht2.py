def data_func(name, surname, birth_year, city, e_mail, ph_numb):
    result = 'Вас зовут {} {}, вы {} г.р., вы из города {} ваша почта  {}, тел. {}'.format(name, surname, birth_year, city, e_mail, ph_numb)
    return result

name = input('Введите имя')
surname = input('Введите фамилию')
birth_year = input('Введите год рождения')
city = input('Введите город проживания')
e_mail = input('Введите свой e-mail')  # предусмотреть форму ввода
ph_numb = input('Введите свой номер телефона')

print(data_func(name, surname, birth_year, city, e_mail, ph_numb))
