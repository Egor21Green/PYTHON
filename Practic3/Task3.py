# 2. Задайте список. Напишите программу, которая определит, присутствует ли в
# заданном списке строк некое число.
# ['22', '33', '123', 'fwefe', 'ytyy', '55']

# f(n)

our_list = ['22', '33', '123', 'fwefe', 'ytyy', '55']
u = 55

for i in range(len(our_list)):
    if our_list[i].isdigit() and int(our_list[i]) == u:
        print(f"В списке присутствует искомое значение.\nНа позиции {i}")
    
