list1 = ['4', 'dfsdf', 'kh43', 'dfsdf']
list2 = ['456', 'dfsdf', '89']

print([k for k in list1 if list2.count(k) < 1])
