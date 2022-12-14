number = input('Введите число: ')
summa = 0
for i in number:
    if i.isdigit():
        summa += int(i)
        print(summa)