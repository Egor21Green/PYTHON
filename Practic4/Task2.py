# Используем filter
# 2. Напишите программу, удаляющую из текста все слова, содержащие "абв"

txt = 'Привет абвгдейка абв абверуеймя вместе с тобой'

a = ' '.join(list(filter(lambda x: not 'абв' in x, txt.split())))
print(a)