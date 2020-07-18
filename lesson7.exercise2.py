rand_list = [-28, -21, -48, 3, -34, 42, 7, 38, 46, -6, 50, 34, -30, -17,
             -6, 46, -21, -31, -2, -40]

result_list = [n for n in rand_list if not n % 3 and n > 0 and n % 4]
print(f'result list:\n{result_list}')
