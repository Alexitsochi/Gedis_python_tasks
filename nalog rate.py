REG_NALOG_RATE = 0.025
FED_NALOG_RATE = 0.05

buy = int(input("Введите сумму покупки: ",))

print(f"Сумма покупки - {buy}")

fed_nalog = buy * FED_NALOG_RATE
print(f"Сумма федерального налога - {fed_nalog}")

reg_nalog = buy * REG_NALOG_RATE
print(f"Сумма регионального налога - {reg_nalog}")

sum_nalog = fed_nalog + reg_nalog
print(f"Общий налог - {sum_nalog}")

total_sum = buy + sum_nalog
print(f"Общая сумма продажи - {total_sum}")
