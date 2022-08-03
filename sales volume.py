NALOG_RATE = 0.07

product_1 = float(input("Введите цену товара один: ",))
product_2 = float(input("Введите цену товара два: ",))
product_3 = float(input("Введите цену товара три: ",))
product_4 = float(input("Введите цену товара четыре: ",))
product_5 = float(input("Введите цену товара пять: ",))

sum = product_1 + product_2 + product_3 + product_4 + product_5
print(f"Общая стоимость товаров: {sum}")

nalog = sum * NALOG_RATE
print("Сумма налога", format(nalog, ".1f"))

total_sum = sum + nalog
print("Итоговая сумма", total_sum)
