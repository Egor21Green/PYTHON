#  Напишите программу, удаляющую из файла все слова, содержащие "абв".

def read_pol(file):
    with open(str(file), 'r', encoding ='utf-8') as data:
        pol = data.read()
    return pol

file_ = 'Home_work5_Tast1.txt'
str_ = read_pol(file_)
print(str_)
a = ' '.join(list(filter(lambda x: not 'абв' in x, str_.split())))  
print(a) 

with open(str(file_), 'w', encoding ='utf-8') as f:
    f.writelines(a)