#  Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# *Пример*

# - при N=236     ->        [2, 2, 59]

num_enter = int(input('Введите число: '))
lst_num = []
d = 2

while d * d <= num_enter:
    if num_enter % d == 0:
        lst_num.append(d)
        num_enter //= d
    else:
        d += 1   
         
if num_enter > 1:
    lst_num.append(num_enter)

print(lst_num)