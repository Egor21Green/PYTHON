from random import randint


def mix(lst):
    for i in range(len(lst)):
        new_i = randint(0, len(lst)-1)
        lst[i], lst[new_i] = lst[new_i], lst[i]


lst_ = [1, 2, 3, 4, 5, 6]
mix(lst_)
print(lst_)