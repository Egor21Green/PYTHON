n = int(input('Введите число: '))
lst = []
sum_ = 0

for i in range(1, n+1):
    count = (1 + 1 / i) ** i
    sum_ = sum_ + count
    lst.append(count)

print(lst)
print(sum_)
