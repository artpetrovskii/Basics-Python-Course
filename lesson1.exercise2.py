number = int(input())

while number not in range(0, 10):
    print('Неверный ввод. Число должно быть [0, 10). Попробуйте снова')
    number = int(input())

else:
    print(number ** 2)
