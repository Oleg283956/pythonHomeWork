team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

name_team1 = 'Мастера кода'
name_team2 = 'Волшебники данных'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'


print('В команде %s участников: %s!' %(name_team1,team1_num))
print('Итого сегодня в командах участников: %s и %s!' %(team1_num,team2_num))

print('Команда {} решила задач: {}!'.format(name_team2,score_2))
print('{} решили задачи за {} с!'.format(name_team2,team2_time))

print(f'Команды решили {score_1} и {score_2} задач.')

print(f'Результат битвы: {challenge_result[0:14].lower()+' '+name_team1}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {(team1_time + team2_time)/tasks_total} секунды на задачу!.')