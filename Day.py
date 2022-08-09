"""Определение дня недели по числу"""

number = int(input("Введите число в диапазоне от 1 до 7: ",))

if number < 1 or number > 7:
    print("Ошибка, номер вне диапазона")
elif number == 1:
    print("Понедельник")
elif number == 2:
    print("Вторник")
elif number == 3:
    print("Среда")
elif number == 4:
    print("Четверг")
elif number == 5:
    print("Пятница")
elif number == 6:
    print("Суббота")
elif number == 7:
    print("Воскресенье")
