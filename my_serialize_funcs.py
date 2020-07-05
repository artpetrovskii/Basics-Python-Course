import os
import pickle
import json


def get_json_from_data(data):
    return json.dumps(data)


def get_data_from_json(json_):
    return json.loads(json_)


def put_json_data_to_file(data, filename, encoding='utf-8'):
    with open(filename, 'w', encoding=encoding) as out_f:
        json.dump(data, out_f)


def get_json_data_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as in_f:
            return json.load(in_f)
    else:
        info = f'file {filename} not exists!'
        return info


def get_pickle_from_data(data):
    return pickle.dumps(data)


def get_data_from_pickle(pickle_):
    return pickle.loads(pickle_)


def put_pickle_data_to_file(data, filename):
    with open(filename, 'wb') as out_f:
        pickle.dump(data, out_f)


def get_pickle_data_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as in_f:
          return pickle.load(in_f)
    else:
        info = f'file {filename} not exists!'
        return info
