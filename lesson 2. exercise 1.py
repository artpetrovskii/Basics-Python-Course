list1 = ['4', 'dfsdf', 'kh43', 'vlof', 'dfsdf']
list2 = ['456', 'dfsdf', '89']

for item in list2:
    if item in list1:
        list1.remove(item)
print(list1)
