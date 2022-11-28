number = int(input('Введите число: '))
summa = 0

while number > 0:
    digit = number % 10
    summa = summa + digit
    number = number // 10

print('Сумма цифр числа - ', summa)