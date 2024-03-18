import os
import shutil
import tkinter as tk
from tkinter import filedialog

working_directory = 'C:/Users/maxim/PycharmProjects/lab2/simple_file_manager'

root = tk.Tk()
root.title("Простой файловый менеджер")


def create_folder(folder_name):
    folder_path = os.path.join(working_directory, folder_name)
    os.mkdir(folder_path)
    print(f"Папка {folder_name} была создана по адресу {folder_path}")


def delete_folder(folder_name):
    folder_path = os.path.join(working_directory, folder_name)
    os.rmdir(folder_path)
    print(f"Папка {folder_name} была удалена из {working_directory}")


def change_folder(folder_name):
    global working_directory
    if folder_name == '..':
        working_directory = os.path.dirname(working_directory)
        print("Поднялись на директорию вверх")
    else:
        new_path = os.path.join(working_directory, folder_name)
        if os.path.exists(new_path) and os.path.isdir(new_path):
            working_directory = new_path
            print(f"Переключились на путь {working_directory}")
        else:
            print(f"Папки не существует")


def create_file(file_name):
    file_path = os.path.join(working_directory, file_name)
    with open(file_path, 'w'):
        pass
    print(f"Файл {file_name} успешно создан")


def write_to_file(file_name, text):
    file_path = os.path.join(working_directory, file_name)
    with open(file_path, 'w') as file:
        file.write(text)
    print(f"Текст успешно записан в файл {file_name}")


def view_file(file_name):
    file_path = os.path.join(working_directory, file_name)
    with open(file_path, 'r') as file:
        content = file.read()
        print(f"Содержимое файла:\n", content)


def delete_file(file_name):
    file_path = os.path.join(working_directory, file_name)
    os.remove(file_path)
    print(f"Файл {file_name} удален")


def copy_file(source_file, destination_folder):
    source_path = os.path.join(working_directory, source_file)
    destination_path = os.path.join(working_directory, destination_folder, source_file)
    shutil.copyfile(source_path, destination_path)
    print(f"файл {source_file} скопирован в {destination_path}")


def move_file(source_file, destination_folder):
    source_path = os.path.join(working_directory, source_file)
    destination_path = os.path.join(working_directory, destination_folder, source_file)
    shutil.move(source_path, destination_path)
    print(f"Файл {source_file} перемещен в {destination_path}")


def rename_file(old_name, new_name):
    old_path = os.path.join(working_directory, old_name)
    new_path = os.path.join(working_directory, new_name)
    os.rename(old_path, new_path)
    print(f"Файл {old_name} переименован в {new_name}")


def fileslist():
    files = os.listdir(working_directory)
    for file in files:
        print(file)


def create_folder_gui():
    folder_name = filedialog.askdirectory()
    create_folder(folder_name)


def delete_folder_gui():
    folder_name = filedialog.askdirectory()
    delete_folder(folder_name)


def change_folder_gui():
    folder_name = filedialog.askdirectory()
    change_folder(folder_name)


def create_file_gui():
    file_name = filedialog.asksaveasfilename(initialdir=working_directory)
    create_file(file_name)


def write_to_file_gui():
    file_name = filedialog.asksaveasfilename(initialdir=working_directory)
    text = input("Введите текст для записи в файл")
    write_to_file(os.path.basename(file_name), text)


def view_file_gui():
    file_name = filedialog.asksaveasfilename(initialdir=working_directory)
    view_file(os.path.basename(file_name))


def delete_file_gui():
    file_name = filedialog.asksaveasfilename(initialdir=working_directory)
    delete_file(os.path.basename(file_name))


def copy_file_gui():
    file_name = filedialog.asksaveasfilename(initialdir=working_directory)
    destination_folder = filedialog.askdirectory()
    copy_file(os.path.basename(file_name), os.path.basename(destination_folder))


def move_file_gui():
    source_file = filedialog.askopenfilename(initialdir=working_directory)
    destination_folder = filedialog.askdirectory()
    move_file(os.path.basename(source_file), os.path.basename(destination_folder))


def rename_file_gui():
    old_name = filedialog.askopenfilename(initialdir=working_directory)
    new_name = input("Введите новое имя файла: ")
    rename_file(os.path.basename(old_name), new_name)


button_create_folder = tk.Button(root, text="Создать папку", command=create_folder_gui)
button_create_folder.pack()

button_delete_folder = tk.Button(root, text="Удалить папку", command=delete_folder_gui)
button_delete_folder.pack()

button_change_folder = tk.Button(root, text="Изменить рабочую папку", command=change_folder_gui)
button_change_folder.pack()

button_create_file = tk.Button(root, text="Создать файл", command=create_file_gui)
button_create_file.pack()

button_write_to_file = tk.Button(root, text="Записать текст в файл", command=write_to_file_gui)
button_write_to_file.pack()

button_view_file = tk.Button(root, text="Просмотреть содержимое файла", command=view_file_gui)
button_view_file.pack()

button_delete_file = tk.Button(root, text="Удалить файл", command=delete_file_gui)
button_delete_file.pack()

button_copy_file = tk.Button(root, text="Копировать файл", command=copy_file_gui)
button_copy_file.pack()

root.mainloop()