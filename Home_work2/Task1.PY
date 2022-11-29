num = input('Введите число: ')
sum = 0

for i in num:
    if i.isdigit():
        sum += int(i)

print(sum)