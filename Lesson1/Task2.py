#Напишите программу, которая принимает на вход координаты
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

print ('Введите координаты X и Y')
x = int(input('Координата Х='))
y = int(input('Координата Y='))
if x == 0 or y == 0:
    print('Нарушение условия задачи')
else:
    if x > 0 and y > 0:
        print('1 четверть')
    elif x < 0 and y > 0:
        print('2 четверть')
    elif x < 0 and y < 0:
        print('3 четверть')
    elif x > 0 and y < 0:
        print('4 четверь')