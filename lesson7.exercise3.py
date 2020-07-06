from math import sqrt


def positive_sqrt(lst):
    return [n if n < 0 else sqrt(n) for n in lst]


rand_list = [-28, -21, -48, 3, -34, 42, 7, 38, 46, -6, 50, 34, -30, -17,
             -6, 46, -21, -31, -2, -40]
print(f'new list:\n{positive_sqrt(rand_list)}\n')
print(f'old list:\n{rand_list}')
