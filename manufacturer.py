import sys, os
from scripts import *
from config import Config

if len(sys.argv) <= 1:
    dir = '.\\application'
    filename = 'default_file_name'
elif len(sys.argv) == 2:
    dir = sys.argv[1]
    filename = 'default_file_name'
else:
    dir = sys.argv[1]
    filename = '_'.join(sys.argv[2:])

configs = Config(filename)
venv_dir = dir + '\\venv'
os.makedirs(dir, exist_ok=True)
os.chdir(dir)
create_venv(venv_dir)
create_folders(configs.folders)
create_files(configs.files)
