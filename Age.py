age = float(input("Введите возраст человека: ",))

if age >= 20:
    print("Взрослый")
elif age <= 1:
    print("Младенец")
elif 1 < age < 13:
    print("Ребенок")
elif 13 <= age < 20:
    print("Подросток")
