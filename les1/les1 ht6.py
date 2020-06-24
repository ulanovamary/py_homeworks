a = int(input('введите дистанцию'))
b = int(input('введите дист. для опред дня'))
day = 1
#print(f'{day}-й день : {a}')

while a < b:
    day += 1
    day_track = a + (a*0.1)
    a = day_track
    #print(f'{day} -й день : {day_track}')
print(day)

