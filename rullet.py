number_rullet = int(input("Введите номер рулетки: ",))

if number_rullet == 0:
    print("Зеленый")
elif 1 <= number_rullet <= 10:
    if number_rullet % 2 == 0:
        print("Черный")
    else:
        print("Красный")
elif 11 <= number_rullet <= 18:
    if number_rullet % 2 == 0:
        print("Красный")
    else:
        print("Черный")
elif 19 <= number_rullet <= 28:
    if number_rullet % 2 == 0:
        print("Черный")
    else:
        print("Красный")
elif 29 <= number_rullet <= 36:
    if number_rullet % 2 == 0:
        print("Красный")
    else:
        print("Черный")
else:
    print("Число вне диапазона")
