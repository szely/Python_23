from rename_files import rename_file as rf
import os
from pathlib import Path

directory_way = Path(Path('/Users/a1234/PycharmProjects/pythonProject_GB/files/my_files'))
new_name = 'my_file'
count_digit = 3
old_expansion = 'txt'
new_expansion = 'txt'
list_rename = [0, 5]

rf(new_name, directory_way, count_digit, old_expansion,new_expansion, list_rename)
