num = int(input('Введите число: '))
list = [1]

for i in range (1,num):
    list.append ((i+1) * list [i-1])

print(list)

