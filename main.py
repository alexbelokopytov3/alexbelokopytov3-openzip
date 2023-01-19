import codecs
from zipfile import ZipFile
import os

os.chdir('.')
dir_list = os.listdir('file')

for archive in dir_list:

    print('Началась распаковка ', archive, '!')

    with ZipFile('file/' + archive, "r") as myzip:
        path = str('open/' + archive.rstrip('.zip'))
        myzip.extractall(path)
    
    print('Расспаковка ', archive, ' завершена!')
    
print('Распаковка архивов завершена!')

dir_list = os.listdir('open')

os.chdir('open')
for folder in dir_list:

    try:
        print('Переименование ', folder, ' началось!')
        properties_path = str(folder + '/Properties.txt')
        properties = open(properties_path, 'r', encoding='cp1251')
        read_properties = properties.readlines()
        properties.close()

        modify_date = read_properties[-1].split('=')
        split_modify_date = modify_date[-1].split(' ')

        folder_name = str('date(' + split_modify_date[0] + ') time ' + split_modify_date[-1].replace(':', '.') )
        folder_name = folder_name.rstrip('\n')

        print(folder_name)
        print(folder)

        folder = str(folder)
        os.rename(folder,folder_name)
        print('Переименование ', folder,' в ', folder_name, ' завершилось!')
    except:
        print('Сбой в переименовании ', folder, '!')