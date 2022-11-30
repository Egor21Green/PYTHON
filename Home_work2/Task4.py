n_first = int(input('Введите левую границу списка: '))
n_second = int(input('Введите правую границу списка: '))
lst = []
if n_first < 0 and n_second > 0:
    
    for i in range(n_first, n_second + 1):
        lst.append(n_first)
        n_first = n_first + 1

else:
    print('Заданные параметры не соответствуют условию')

N_first = int(input('Введите левую границу списка: '))
N_second = int(input('Введите правую границу списка: '))

# Чуть позже
...