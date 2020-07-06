def game_inversed():
    # версия с проверками корректности вводимых данных

    from random import randint

    num_min = 1
    num_max = 100
    num_start = num_min
    num_stop = num_max
    attempts = 0
    operands = {
        'smaller': '<',
        'bigger': '>',
        'right': '='
    }

    print('Модификация игры "Угадай число"')
    print(f'В этой версии игры человек загадывает число, а компьютер пытается его угадать.')

    while True:
        guess_num = input(f'Введите загаданное число от {num_min} до {num_max}: ')
        if not guess_num.isdigit():
            print('Вы ввели не число!')
        elif not num_min <= int(guess_num) <= num_max:
            print('Вы ввели число за пределами указанного диапазона!')
        else:
            guess_num = int(guess_num)
            break

    print('\nКомпьютер начинает угадывать число...')
    print(f"Вводите с клавиатуры {operands['bigger']}, {operands['smaller']} или {operands['right']}\n")

    operand = None
    while operand != operands['right']:
        random_num = randint(num_start, num_stop)
        attempts += 1

        while True:
            operand = input(f'Число {random_num} больше, меньше или равно загаданному? \n')
            if (random_num > guess_num and operand == operands['bigger']) \
                    or (random_num < guess_num and operand == operands['smaller']) \
                    or (random_num == guess_num and operand == operands['right']):
                if operand == operands['bigger']:
                    num_stop = random_num - 1
                elif operand == operands['smaller']:
                    num_start = random_num + 1
                break
            else:
                print('Вы ошиблись при вводе символа сравнения загаданного числа с предложенным.\nПроверьте себя и '
                      'повторите ввод.')

    result = f'Компьютер угадал Ваше число с {attempts}-й попытки!'
    print()
    print(result)
    return result


if __name__ == '__main__':
    game_inversed()
