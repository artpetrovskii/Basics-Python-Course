import os

def create_forlders(n):
    for i in range(1, n+1):
        folder_name = 'folder_{:02}'.format(i)
        os.mkdir(folder_name)
        print(f'created folder: {folder_name}')
print('donen\n')

def delete_forlders(n):
    for i in range(1, n+1):
        folder_name = 'folder_{:02}'.format(i)
        os.rmdir(folder_name)
        print(f'deleted folder: {folder_name}')
print('done\n')

print('"my_folders.py" imported ')
if __name__ == '__main__':
    create_forlders(9)
    delete_forlders(9)
