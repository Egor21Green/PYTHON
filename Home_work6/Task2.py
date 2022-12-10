# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint


# number = int(input('Введите размер списка '))
# lst_1 = []
# lst_2 = []

# for i in range(number):
#     lst_1.append(randint(0, 9))

# for i in range(len(lst_1)):
#     while i < len(lst_1)/2 and number > len(lst_1)/2:
#         number = number - 1
#         a = lst_1[i] * lst_1[number]
#         lst_2.append(a)
#         i += 1

# print(lst_1)
# print(lst_2)

import math
list_a = list(map(int, input('Введите числа, через пробел: ').split()))
print('Исходный список: ',list_a)
print('Результат: ',list([a * b for a, b in zip(list_a[0:math.ceil(len(list_a) / 2)],list_a[::-1])]))