# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = [2, 3, 5, 9, 3, 2, 1, 2]
i = 1
sum = 0
while i < len(lst):
    sum = sum + lst[i]
    i += 2

print(sum)