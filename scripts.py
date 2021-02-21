import venv, os

def create_venv(dir):
    print(f'Creating venv at {dir}', end=' ')
    try:
        venv_object = venv.EnvBuilder(with_pip=True)
        venv_object.create(dir)
    except Exception:
        print('--- Error')
    else:
        print('--- Done')

def create_folders(folder_list):
    for folder in folder_list:
        print(f'Makin {folder} folder', end=' ')
        try:
            os.makedirs(folder)
        except Exception:
            print('--- Error')
        else:
            print('--- Done')

def create_files(file_list):
    for file in file_list:
        print(f'Makin {file} file', end=' ')
        try:
            with open(file, 'a') as file:
                pass
        except Exception:
            print('--- Error')
        else:
            print('--- Done')