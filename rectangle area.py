rectangle_x1 = int(input("Введите длину 1 прямоугольника: ",))
rectangle_y1 = int(input("Введите ширину 1 прямоугольника: ",))

rectangle_x2 = int(input("Введите длину 2 прямоугольника: ",))
rectangle_y2 = int(input("Введите ширину 2 прямоугольника: ",))

rectangle_1 = rectangle_x1 * rectangle_y1
rectangle_2 = rectangle_x2 * rectangle_y2

if rectangle_1 == rectangle_2:
    print("Площади прямоугольников равны")
elif rectangle_1 > rectangle_2:
    print("Площадь первого прямоугольника больше")
else:
    print("Площадь второго прямоугольника больше")
