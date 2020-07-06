print("Введите имя: ")
name = input()
print("Введите фамилию: ")
surname = input()
print("Введите возраст: ")
while True:
    try:
        age = int(input())
        if 0 < age < 150:
            break
        else:
            print("Введено некорректно значение. Попробуйте еще раз")

print("Введите вес: ")
while True:
    try:
        weight = int(input())
        if 0 < weight < 150:
            break
        else:
            print("Введено некорректно значение. Попробуйте еще раз")

print("Пациент: ", name, " ", surname, ". Возраст: ", age, ". Вес : ", weight)

if age < 30 and 50 <= weight <= 70:
    print("Хорошее состояние")
elif (age > 30 and weight < 50) or (age > 30 and weight > 90):
    print("Следует заняться собой")
else:
    print("Не парься :)")
