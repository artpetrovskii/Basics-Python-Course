my_list_1 = [1, 2, 3, 4, 5]
my_list_2 = [2, 3, 4, 5, 6, 7, 8]
for item in my_list_2:
    if item in my_list_1:
        my_list_1.remove(item)
print(my_list_1)
print(my_list_2)
