# Игра в загадки

mys1 = 'Как зовут карлика из "Игры престолов"? '
mys2 = 'Как зовут классика, победителя 17-го независимого? '
mys3 = 'Сколько будет 2 + 2 * 2 ? '
mys4 = '---- раз отмерь, один раз отрежь '
mys5 = 'Что без труда не вытащить из пруда? '

ques1 = input(mys1)
if ques1 == 'Тирион' or ques1 == 'тирион':
    print('Хорошее начало! Это действительно его имя!')
    ques1 = 1
    ques2 = input(mys2)
else:
    print('НЕТ!')
    ques1 = 0
    ques2 = input(mys2)

if ques2 == 'Витя' or ques2 == 'витя' or ques2 == 'Виктор' or ques2 == 'виктор':
    print('Оу, да вы знаток')
    ques2 = 1
    ques3 = input(mys3)
else:
    print('Хотелось бы, но увы нет!')
    ques2 = 0
    ques3 = input(mys3)

if ques3 == '6':
    print('А Вы не прогуливали школу!')
    ques3 = 1
    ques4 = input(mys4)
else:
    print('Вам нужно повторить математику!')
    ques3 = 0
    ques4 = input(mys4)

if ques4 == '7' or ques4 == 'семь' or ques4 == 'Семь':
    print('Великолепно!')
    ques4 = 1
    ques5 = input(mys5)
else:
    print('Увы!')
    ques4 = 0
    ques5 = input(mys5)

if ques5 == 'Рыбку' or ques5 == 'рыбку' or ques5 == 'рыбу' or ques5 == 'Рыбу':
    print('Потрясно!')
    ques5 = 1
else:
    print('Не верно')
    ques5 = 0

result = ques1 + ques2 + ques3 + ques4 + ques5
print('\nИтак, наша викторина подошла к концу!\n По итогам игры вы дали ' + str(result) + ' верных ответов!')

