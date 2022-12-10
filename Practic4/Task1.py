#  Используем map
# 1. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие
# A[i] - 1 = A[i-1]. Найдите это число.

# 5 6 7 8 9 10 12 13
# count = None

# with open('text.txt') as f:
#     for item in map(int, f.read().split( )):
#         if count is None:
#             count = item
#         else:
#             if item != count + 1:
#                 print(count + 1) 
#             count = item      
with open("text.txt", "r") as f:
    lst = list(map(int, f.read().split()))

res = 0
for key, item in enumerate(lst):
    if key + 1 < len(lst) and item + 1 != lst[key + 1]:
     res = item + 1

print(res)