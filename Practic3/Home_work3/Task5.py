# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def Fibonachi(n):
    if n in [1, 2]:                       
        return 1
    else:
        return Fibonachi(n-1) + Fibonachi(n-2)

def Negative_Fibonachi(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num_1, num_2 = 1, -1
        for i in range(2, n):
            num_1, num_2 = num_2, num_1 - num_2
        return num_2

lst = [0]
number = int(input('Введите число: '))
for i in range(1, number + 1):
    lst.append(Fibonachi(i))
    lst.insert(0, Negative_Fibonachi(i))
print(lst)