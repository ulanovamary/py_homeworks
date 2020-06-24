user_answer = int(input('Введите количество секунд для перевода в формат чч:мм:сс.'))
seconds = int(user_answer%60)
minutes = int(((user_answer - seconds)/60)%60)
hours = int((user_answer-seconds-minutes*60)/3600)
print('{} : {} : {}'.format(hours,minutes, seconds))


