SOUSAGE_PACK = 10
BUN_PACK = 8

people = int(input("Введите количество людей: ",))
hotdogs = int(input("Введите количество хот-догов каждому человеку: ",))
count_hotdogs = people * hotdogs

if count_hotdogs != 0:
    if count_hotdogs % 10 == 0:
        min_pak_sosisok = count_hotdogs // SOUSAGE_PACK
        print("Минималльное количество упаковок с сосисками:",
              f"{min_pak_sosisok}, осталось сосисок {count_hotdogs % SOUSAGE_PACK}")
    else:
        min_pak_sosisok = count_hotdogs // SOUSAGE_PACK + 1
        print("Минималльное количество упаковок с сосисками:",
              f"{min_pak_sosisok}, осталось сосисок {SOUSAGE_PACK - count_hotdogs % SOUSAGE_PACK}")

if count_hotdogs != 0:
    if count_hotdogs % 8 == 0:
        min_pak_bulochek = count_hotdogs // BUN_PACK
        print("Минималльное количество упаковок с булочками:",
            f"{min_pak_bulochek}, осталось булочек {count_hotdogs % BUN_PACK}")
    else:
        min_pak_bulochek = count_hotdogs // BUN_PACK + 1
        print("Минималльное количество упаковок с булочками:",
            f"{min_pak_bulochek}, осталось булочек {BUN_PACK - count_hotdogs % BUN_PACK}")
