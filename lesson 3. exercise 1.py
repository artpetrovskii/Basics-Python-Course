import random

<<<<<<< HEAD
    begin = 1
    end = 100
    is_repeat = False
    input("Задумайте любое число от 1 до 100 и запишите"
          " его на бумаге. \n Как будете готовы, нажмите 'ввод'")

    
    def game():
        print("Я программа угадывающая числа от 1 до 100")


    guesses = {1: "Я предположу, что вы загадали {}?",
               2: "Ммм... может {} загаданное число?",
               3: "{}! Я чувствую это! Вы загадали именно это число!"}
=======
begin = 1
end = 100
is_repeat = False
print("Я программа угадывающая числа от 1 до 100")
input("Задумайте любое число от 1 до 100 и запишите"
      " его на бумаге. \n Как будете готовы, нажмите 'ввод'")

guesses = {1: "Я предположу, что вы загадали {}?",
           2: "Ммм... может {} загаданное число?",
           3: "{}! Я чувствую это! Вы загадали именно это число!"}
>>>>>>> Lesson3

victory = {1: "Ура! Я угадал",
           2: "Хаха. Это было совсем не сложно",
           3: "Само собой! Но давай я займусь чем-нибудь полезным"}

fails = {1: "О нет",
         2: "Черт",
         3: "Ну как так"}

angry = {1: "Ненавижу тебя!",
         2: "Что б вы все сгорели!",
         3: "Что и следовало ожидать"}

<<<<<<< HEAD
    while True:
        if begin > end:
            print("Ошибка")
            break
        if not is_repeat:
            version = random.randint(begin, end)
        print(guesses[random.randint(1, 3)].format(version))
        user_answer = input("1: Ты угадал! 5: Недобор! 9: Перебор!\n")
        if user_answer == '1':
            print(victory[random.randint(1, 3)])
            break
        elif user_answer == '5':
            print(fails[random.randint(1, 3)])
            begin = version + 1
            is_repeat = False
        elif user_answer == '9':
            print(fails[random.randint(1, 3)])
            end = version - 1
            is_repeat = False
        else:
            print("Неверный ввод")
            is_repeat = True
=======
while True:
    if begin > end:
        print(angry[random.randint(1, 3)])
        break
    if not is_repeat:
        version = random.randint(begin, end)
    print(guesses[random.randint(1, 3)].format(version))
    user_answer = input("1: Ты угадал! 5: Недобор! 9: Перебор!\n")
    if user_answer == '1':
        print(victory[random.randint(1, 3)])
        break
    elif user_answer == '5':
        print(fails[random.randint(1, 3)])
        begin = version + 1
        is_repeat = False
    elif user_answer == '9':
        print(fails[random.randint(1, 3)])
        end = version - 1
        is_repeat = False
    else:
        print(angry[random.randint(1, 3)])
        is_repeat = True
>>>>>>> Lesson3
