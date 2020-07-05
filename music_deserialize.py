import my_serialize_funcs as msf

data_pickle_filename = 'my_group.pickle'
data_json_filename = 'my_group.json'

group_data_from_pickle_file = msf.get_pickle_data_from_file(data_pickle_filename)
my_group_from_pickle = msf.get_data_from_pickle(group_data_from_pickle_file)
print(f'\nmy group from pickle:\n{my_group_from_pickle}')
print(type(my_group_from_pickle))

group_data_from_json_file = msf.get_json_data_from_file(data_json_filename)
my_group_from_json = msf.get_data_from_json(group_data_from_json_file)
print(f'\nmy group from json:\n{my_group_from_json}')
print(type(my_group_from_json))

if my_group_from_pickle == my_group_from_json:
    print('\ndata from json and from pickle is equal')
