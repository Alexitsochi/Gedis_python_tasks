"""Программа подсчета монет, введенных пользователем, равных 1 рублю"""

coins_5 = int(input("Введите количество монет номиналом 5 копеек: ",))
coins_10 = int(input("Введите количество монет номиналом 10 копеек: ",))
coins_50 = int(input("Введите количество монет номиналом 50 копеек: ",))

coins_sum = (5 * coins_5) + (10 * coins_10) + (50 * coins_50)

if coins_sum == 100:
    print("Поздравляем, вы набрали один рубль")
else:
    if coins_sum < 100:
        print("Вы ввели сумму меньше рубля")
    else:
        print("Вы ввели сумму больше рубля")




