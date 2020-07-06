import sys
import os
from core import mkfile, mkdir, ls, delete, copy, log, cd, get_cwd, save_cwd
import game_inversed

info = ''
dwd = os.getcwd()  # default working directory
cwd_file_name = 'path.txt'
log_file_name = 'log.txt'
cwd_file_full = os.path.join(dwd, 'data', cwd_file_name)
log_file_full = os.path.join(dwd, log_file_name)

cwd = get_cwd(cwd_file_full) or os.getcwd()  # current working directory

try:
    command = sys.argv[1]
except IndexError:
    print('Укажите команду в качестве аргумента запускаемого файла')
    print(info)
else:
    if command == 'ls':
        files, folders = True, True
        if len(sys.argv) > 2:
            if sys.argv[2] == 'folders':
                ls(cwd, files=False)
                log(log_file_full, f'Запрошен состав директории (только папки) {cwd}')
            elif sys.argv[2] == 'files':
                ls(cwd, folders=False)
                log(log_file_full, f'Запрошен состав директории (только файлы) {cwd}')
        else:
            ls(cwd)
            log(log_file_full, f'Запрошен состав директории (папки и файлы) {cwd}')

    elif command == 'mkfile':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Укажите имя создаваемого файла вторым аргументом')
        else:
            fullname = os.path.join(cwd, name)
            mkfile(fullname)
            log(log_file_full, f'Создан файл {name} в папке {cwd}')

    elif command == 'mkdir':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Укажите имя создаваемой папки вторым аргументом')
        else:
            fullname = os.path.join(cwd, name)
            mkdir(fullname)
            log(log_file_full, f'Создана папка {name} в папке {cwd}')

    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Укажите имя удаляемой папки или файла вторым аргументом')
        else:
            fullname = os.path.join(cwd, name)
            delete(fullname)
            log(log_file_full, f'{name} удалён из {cwd}')

    elif command == 'copy':
        try:
            name = sys.argv[2]
            name_new = sys.argv[3]
        except IndexError:
            print('Укажите исходное и новое имя файла или папки вторым и третьим аргументами')
        else:
            fullname = os.path.join(cwd, name)
            fullname_new = os.path.join(cwd, name_new)
            copy(fullname, fullname_new)
            log(log_file_full, f'Создана копия {name} с именем {name_new} в папке {cwd}')

    elif command == 'cd':
        if len(sys.argv) > 2:
            name = sys.argv[2]
            cwd = cd(name)
            save_cwd(cwd_file_full, cwd)
            log(log_file_full, f'Директория изменена на {cwd}')
        else:
            cwd = cd(dwd)
            save_cwd(cwd_file_full, cwd)
            log(log_file_full, f'Директория изменена на директорию консольного файлового менеджера')

    elif command == 'game':
        game_title = 'Угадай число (наоборот)'
        log(log_file_full, f'Запуск игры "{game_title}"')
        game_result = game_inversed()
        log(log_file_full, f'Окончание игры "{game_title}". {game_result}')

    elif command == 'help':
        print(info)

    else:
        print('Неизвестная команда')
        print(info)
