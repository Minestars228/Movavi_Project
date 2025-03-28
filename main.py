import sys

f = open('score.txt', 'r+')
f.truncate(0)

count_easy = 0
count_medium = 0
count_hard = 0

print('Привет дорогой друг!\nТы пришёл на викторину по ВОВ(Великой Отечественной Войне)')

player_name = input('Введите своё имя >> ')

print(f'Добро пожаловать в викторину {player_name}')
while True:
    while True:
        try:
            if count_easy >= 1 and count_medium >= 1 and count_hard >= 1:
                print('Поздравляю вы прошли всю викторину на всех уровнях сложности!')
                print('Вот ваши результаты\n')
                file_2 = open('score.txt', mode='r', encoding='utf-8')
                text = file_2.read()
                file_2.close()
                print(text)
                print('\nНа этом викторина заканчивается')
                print('До свидания')
                sys.exit()
            else:
                difficulty = None
                hard_mode = int(input('Выберите уровень сложности: \n    1) Легкий\n    2) Средний\n    3) Сложный\nВведите цифру варианта ответа >> '))
                if count_easy == 0:
                    if hard_mode == 1:
                        difficulty = 'легкий'
                        count_easy += 1
                        break
                else:
                    print('Вы уже прошли этот уровень сложности!')
                if count_medium == 0:
                    if hard_mode == 2:
                        difficulty = 'средний'
                        count_medium += 1
                        break
                else:
                    print('Вы уже прошли этот уровень сложности!')
                if count_hard == 0:
                    if hard_mode == 3:
                        difficulty = 'сложный'
                        count_hard += 1
                        break
                else:
                    print('Вы уже прошли этот уровень сложности!')
        except ValueError:
            print('Введите пожалуйста цифру!!!')

    print(f'Вы выбрали уровень сложности: {difficulty}!\n')



    class hard_mode_class:
            def hard_mode_funcions():
                global player_name
                global difficulty
                if difficulty == 'легкий':
                    import easy
                    file = open('score.txt', mode='a', encoding='utf-8')
                    file.write(f'Сложность: легкая \nИмя игрока: {player_name}\nКоличество очков в викторине: {easy.score}/{easy.questions_count}\n')
                    file.close()
                    file_2 = open('score.txt', mode='r', encoding='utf-8')
                    text = file_2.read()
                    file_2.close()
                    print(text)
                    while True:
                        next = input('Хотите ли вы ещё поучавствовать в викторине? >> ')
                        if next.lower().strip() == 'да':
                            print('Хорошо продолжаем викторину')
                            break
                        elif next.lower().strip() == 'нет':
                            sys.exit()
                elif difficulty == 'средний':
                    import medium
                    file = open('score.txt', mode='a', encoding='utf-8')
                    file.write(f'Сложность: средняя \nИмя игрока: {player_name}\nКоличество очков в викторине: {medium.score}/{medium.questions_count}\n')
                    file.close()
                    file_2 = open('score.txt', mode='r', encoding='utf-8')
                    text = file_2.read()
                    file_2.close()
                    print(text)
                    while True:
                        next = input('Хотите ли вы ещё поучавствовать в викторине? >> ')
                        if next.lower().strip() == 'да':
                            print('Хорошо продолжаем викторину')
                            break
                        elif next.lower().strip() == 'нет':
                            sys.exit()
                elif difficulty == 'сложный':
                    import hard
                    file = open('score.txt', mode='a', encoding='utf-8')
                    file.write(f'Сложность: сложная \nИмя игрока: {player_name}\nКоличество очков в викторине: {hard.score}/{hard.questions_count}\n')
                    file.close()
                    file_2 = open('score.txt', mode='r', encoding='utf-8')
                    text = file_2.read()
                    file_2.close()
                    print(text)
                    while True:
                        next = input('Хотите ли вы ещё поучавствовать в викторине? >> ')
                        if next.lower().strip() == 'да':
                            print('Хорошо продолжаем викторину')
                            break
                        elif next.lower().strip() == 'нет':
                            sys.exit()


    hard_mode_class.hard_mode_funcions()
