import my_folders
import my_random

my_folders.create_forlders(9)
my_folders.delete_forlders(9)
print(f'random element from non-empty list: {my_random.get_random_element([1, 2, 3, 4])}')
print(f'random element from empty list: {my_random.get_random_element([])}')