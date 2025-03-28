import random

def medium_funcion():
    global score
    global questions_count
    score = 0
    count = 0
    questions_medium = ["Когда началась Вторая мировая война?","Кто победил во Второй мировой войне?","Какая страна не принимала участия во Второй мировой войне?","В какой стране зародился фашизм?","Какая страна потеряла больше всего людей во Второй мировой войне?","Самая продолжительная битва Второй мировой войны.","Сколько евреев служило в армии США?","Какая битва Второй мировой войны стала крупнейшим сражением американских войск?","Сколько человек убили нацисты?","«Божественный ветер» во Вторую мировую войну — это ..."]
    answer_options = ["1924\n1941\n1991","СССР, Франция, Италия и США\nВсе страны оси\nСССР, США, Великобритания","Аргентина\nИталия\nЯпония","Германия\nИталия\nЯпония","США\nГермания\nСССР","Битва за Атлантику\nБитва за Берлин\nСталинградская битва","Около 600 000\nПримерно 10 000\nЧуть больше 2 000","Битва за Эниветок\nБитва в Арденнах\nБитва за Лусон","Около 12 миллионов\nОколо 2 миллиардов\nОколо 5 миллионов","Японские камикадзе\nПодразделение военно-воздушных сил США\nОперация Третьего рейха"]
    correct_answer_options = ["1941","СССР, США, Великобритания","Аргентина","Италия","СССР","Битва за Атлантику","Около 600 000","Битва в Арденнах","Около 12 миллионов","операция Третьего рейха"]
    questions_count = len(questions_medium)
    print('Примечание: когда вам предлагается вариант ответа номер варианта ответа, а не сам ответ')
    for _ in range(len(questions_medium)):
        count_2 = 1
        count_3 = 0
        print(questions_medium[count])
        random_answer_options = answer_options[count].split('\n')
        random.shuffle(random_answer_options)
        for _ in range(len(random_answer_options)):
            print(f'{count_2}) {random_answer_options[count_3]}')
            count_2 += 1
            count_3 += 1
        while True:
            try:
                player_answer = int(input('Введите ответ >> '))
                if random_answer_options[player_answer - 1].lower() == correct_answer_options[count].lower():
                    score += 1
                    print(f'\nПоздравляю, вы ответили правильно!')
                    print(f'Вы ответили правильно на {score}/{len(questions_medium)}\n')
                    break
                else:
                    print(f'\nУвы, вы ответили не правильно(((')
                    print(f'Правильный ответ - {correct_answer_options[count]}\n')
                    break
            except:
                print('Бирибилька')
                print('Ведите цифру от 1 до 3')
        count += 1
    print(f'На этом викторина заканчивантся ваш счет {score}/{questions_count}')
    print('Спасибо что поучавствовали в викторине по Великой Отечественной Войне')

medium_funcion()
