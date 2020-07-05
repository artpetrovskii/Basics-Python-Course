import my_serialize_funcs as msf
import os

my_favourite_group = {
    'name': 'Lacuna Coil',
    'genre': 'gothic metal',
    'members': [
        {'name': 'Andrea Ferro',
         'role': 'male vocals'},
        {'name': 'Marco Coti Zelati',
         'role': 'bass, keyboards'},
        {'name': 'Cristina Scabbia',
         'role': 'female vocals'},
        {'name': 'Diego "Didi" Cavalotti',
         'role': 'guitars'},
        {'name': 'Richard Meiz',
         'role': 'drums'}
    ],
    'albums': [
        {'name': 'In a Reverie',
         'year': 2000},
        {'name': 'Comalies',
         'year': 2006},
        {'name': 'Karmacode',
         'year': 2008},
        {'name': 'Shallow Life',
         'year': 2010},
        {'name': 'Dark Adrenaline',
         'year': 2012},
        {'name': 'Broken Crown Halo',
         'year': 2013},
        {'name': 'Delirium',
         'year': 2016}
    ]
}

data_pickle_filename = 'my_group.pickle'
data_json_filename = 'my_group.json'

group_data_pickle = msf.get_pickle_from_data(my_favourite_group)
print(f'\npickle data:\n{group_data_pickle}')
print(type(group_data_pickle))

msf.put_pickle_data_to_file(group_data_pickle, data_pickle_filename)
if os.path.exists(data_pickle_filename):
    print(f'pickle data written to {data_pickle_filename}')

group_data_json = msf.get_json_from_data(my_favourite_group)
print(f'\njson data:\n{group_data_json}')
print(type(group_data_json))

msf.put_json_data_to_file(group_data_json, data_json_filename)
if os.path.exists(data_json_filename):
    print(f'json data written to {data_json_filename}')
