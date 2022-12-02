# with open('file.txt', 'a') as data:
#     data.write('Line \n')
#     data.write('Line')
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
# exit()    

# def cons(*params):
#     res: str = ""
#     for item in params:
#         res += item
    
#     return res


# print(cons('1','2'))

def fib(n):
    if n in [1,2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)  

lst = []  
for e in range(1,10):
    lst.append(fib(e))  
print(lst)          