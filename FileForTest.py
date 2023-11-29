import os


directory_cur = 'gallery/files'


def get_files_list(directory):
    return os.listdir(directory)


print(get_files_list(directory_cur))