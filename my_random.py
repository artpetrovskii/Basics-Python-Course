import random

def get_random_element(lst):
    if lst:
        return random.choice(lst)


print('"my_random.py" imported ')
if __name__ == '__main__':
    test_list = [0, 1, 2, 3, 4, 5]
    print(get_random_element(test_list))
