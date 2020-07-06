import os
import shutil
import datetime as dt


def mkfile(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def mkdir(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка с таким именем уже существует')


def cd(name):
    try:
        if os.path.isdir(name):
            os.chdir(name)
        else:
            print('Указанная папка не существует')
    except:
        print('Введен некорректный путь к папке')
    return os.getcwd()


def ls(path, folders=True, files=True):
    result = os.listdir(path)
    folders_list = [f for f in result if os.path.isdir(f)]
    files_list = [f for f in result if not os.path.isdir(f)]
    print(f'Директория:\n{path}')

    if folders:
        print('Список папок:')
        print(*folders_list, sep='\n')
    if files:
        print('Список файлов:')
        print(*files_list, sep='\n')


def delete(name):
    try:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
    except FileNotFoundError:
        print('Не удается найти указанный для удаления объект')
    except OSError:
        print('Невозможно удалить объект. Возможно, папка не пуста или заблокирована операционной системой')


def copy(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Папка с таким именем уже существует')
    else:
        shutil.copy(name, new_name)


def log(fullpath, message):
    current_time = dt.datetime.now()
    result = f'{current_time}: {message}'
    with open(fullpath, 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def get_cwd(path_filename):
    result = None
    try:
        with open(path_filename, 'r', encoding='utf-8') as f:
            result = f.readline()
    except FileNotFoundError:
        pass
    return result


def save_cwd(path_filename, path):
    mkfile(path_filename, text=path)


if __name__ == '__main__':
    pass
