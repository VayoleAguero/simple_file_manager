import os
import shutil

working_directory='C:/Users/maxim/PycharmProjects/lab2/simple_file_manager'

def create_folder(folder_name):
    folder_path=os.path.join(working_directory,folder_name)
    os.mkdir(folder_path)
    print(f"Папка {folder_name} была создана по адресу {folder_path}")

def delete_folder(folder_name):
    folder_path = os.path.join(working_directory, folder_name)
    os.rmdir(folder_path)
    print(f"Папка {folder_name} была удалена из {working_directory}")

def change_folder(folder_name):
    global working_directory
    if folder_name=='..':
        working_directory=os.path.dirname(working_directory)
        print("Поднялись на директорию вверх")
    else:
        new_path=os.path.join(working_directory,folder_name)
        if os.path.exists(new_path) and os.path.isdir(new_path):
            working_directory=new_path
            print(f"Переключились на путь {working_directory}")
        else:
            print(f"Папки не существует")

def create_file(file_name):
    file_path=os.path.join(working_directory,file_name)
    with open(file_path,file_name,'w'):
        pass
    print(f"Файл {file_name} успешно создан")

def write_to_file(file_name,text):
    file_path=os.path.join(working_directory,file_name)
    with open(file_path,'w') as file:
        file.write(text)
    print(f"Текст успешно записан в файл {file_name}")

def view_file(file_name):
    file_path=os.path.join(working_directory,file_name)
    with open(file_path,'r') as file:
        content=file.read()
        print(f"Содержимое файла:\n",content)

def delete_file(file_name):
    file_path=os.path.join(working_directory,file_name)
    os.remove(file_path)
    print(f"Файл {file_name} удален")

def copy_file(source_file,destination_folder):
    source_path=os.path.join(working_directory,source_file)
    destination_path=os.path.join(working_directory,destination_folder,source_file)
    shutil.copyfile(source_path,destination_path)
    print(f"файл {source_file} скопирован в {destination_path}")

def move_file(source_file,destination_folder):
    source_path=os.path.join(working_directory,source_file)
    destination_path=os.path.join(working_directory,destination_folder,source_file)
    shutil.move(source_path,destination_path)
    print(f"Файл {source_file} перемещен в {destination_path}")

def rename_file(old_name,new_name):
    old_path=os.path.join(working_directory,old_name)
    new_path=os.path.join(working_directory,new_name)
    os.rename(old_path,new_path)
    print(f"Файл {old_name} переименован в {new_name}")

def fileslist():
    files=os.listdir(working_directory)
    for file in files:
        print(file)



