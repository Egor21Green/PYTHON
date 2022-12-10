lst = []

for x in range(1, 10):
    if not x % 2:
        lst.append(x * x)

print(lst) 

lst2 = [x * x for x in range(1, 10) if not x % 2]
print (lst2)