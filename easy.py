import random

def easy_funcion():
    global score
    global questions_count
    score = 0
    count = 0
    questions_easy = ["Какое сражение считается поворотным моментом войны на Восточном фронте?" , "Какой марш стал символом Великой Отечественной войны?" , "Какое событие произошло 9 мая 1945 года?" , "Кто был верховным главнокомандующим советскими войсками в годы войны?" , "Какой фронт был создан в 1941 году для защиты Москвы?" , "Какое танк использовали советские солдаты в боях?" , "Какие страны были союзниками СССР во время войны?"]
    answer_options = ['Битва под Москвой\nСталинградская битва\nКурская битва\nБитва за Ленинград' , 'Марш энтузиастов\nПрощание славянки\nМарш защитников Москвы\nСвященная война' , 'Начало войны\nОкончание войны\nБитва за Берлин\nПодписание мирного договора' , 'Лев Троцкий\nИосиф Сталин\nГеоргий Жуков\nВасилий Чуйков' , 'Северный фронт\nЗападный фронт\nТри фронта\nЮго-Западный фронт' , 'Танк «Т-34»\nТанк «Пантера»\nТанкетка «БТ»\nТанк «Шерман»' , 'Германия и Италия\nСША и Великобритания\nЯпония и Франция\nИспания и Португалия']
    correct_answer_options = ['Курская битва' , 'Прощание славянки' , 'Окончание войны' , 'Иосиф Сталин' , 'Три фронта' , 'Танк «Т-34»' , 'США и Великобритания']
    questions_count = len(questions_easy)
    print('Примечание: когда вам предлагается вариант ответа номер варианта ответа, а не сам ответ')
    for _ in range(len(questions_easy)):
        count_2 = 1
        count_3 = 0
        print(questions_easy[count])
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
                    print(f'Вы ответили правильно на {score}/{len(questions_easy)}\n')
                    break
                else:
                    print(f'\nУвы, вы ответили не правильно(((')
                    print(f'Правильный ответ - {correct_answer_options[count]}\n')
                    break
            except:
                print('Бирибилька')
                print('Ведите цифру от 1 до 4')
        count += 1
    print(f'На этом викторина заканчивантся ваш счет {score}/{questions_count}')
    print('Спасибо что поучавствовали в викторине по Великой Отечественной Войне')

easy_funcion()
