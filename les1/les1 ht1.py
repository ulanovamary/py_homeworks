my_name = 'Мария'
my_age = 31
your_name = input('What is your name?')
your_age = int(input('How old are you?'))
current_year = int(input('Please, enter a current year'))
birth_year = current_year - your_age

print('Вас зовут {}, Вам {} и Вы родились в {} году'.format(your_name, your_age, birth_year) )
