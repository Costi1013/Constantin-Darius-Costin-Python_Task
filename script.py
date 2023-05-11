import os
import shutil
from datetime import datetime
import schedule
import time

# Creează  "folder1"
folder1 = "Folder1"
if not os.path.exists(folder1):
    os.mkdir(folder1)

# Creează  "folder2"
folder2 = "Folder2"
if not os.path.exists(folder2):
    os.mkdir(folder2)

# source_folder = r"`C:\Users\Costi\Desktop\Task_ConstantinDariusCostin\Folder1\\"
# destination_folder = r"C:\Users\Costi\Desktop\Task_ConstantinDariusCostin\Folder2\\"
# destination_write = r"C:\Users\Costi\Desktop\Task_ConstantinDariusCostin\log.txt"

time_sync = int(input("Seteza timpul de sincronizare:"))
source_folder = input("Scrie calea folderului sursa:")
destination_folder = input("Scrie calea folderului replica:")
destination_write = input("Scrie calea pentru log_file:")

f = open(destination_write, "a+")

def fetch_all_files():
    for file_name in os.listdir(source_folder):
        if os.path.isfile(source_folder + file_name):
            f1 = open(source_folder + file_name, "r")
            f2 = open(destination_folder + file_name, "w+")
            if f1.read() != f2.read():
                f.write(f"In ziua <{datetime.now()}> Fisierul -- {file_name} -- a fost actualizat! \n") #Scriere in fisierul log.txt
                print(f"In ziua <{datetime.now()}> Fisierul -- {file_name} -- a fost actualizat!")
            else:
                f.write(f"In ziua <{datetime.now()}> Fisierul -- {file_name} -- a fost copiat! \n") #Scriere in fisierul log.txt
                print(f"In ziua <{datetime.now()}> Fisierul -- {file_name} -- a fost copiat!")
            shutil.copy(source_folder + file_name, destination_folder + file_name)

    # Verificare daca a fost sters vreun fisier din folderul sursă
    for file_name in os.listdir(destination_folder):
        if os.path.isfile(destination_folder + file_name):
            if not os.path.exists(source_folder + file_name):
                f.write(f"In ziua <{datetime.now()}> Fisierul -- {file_name} -- a fost sters! \n") #Scriere in fisierul log.txt
                print(f"In ziua <{datetime.now()}> Fisierul -- {file_name} -- a fost sters!")
                os.remove(destination_folder + file_name)

# fetch_all_files()

# Sincronizare periodica
schedule.every(time_sync).minutes.do(fetch_all_files)
while True:
    # Executăm sarcinile programate
    schedule.run_pending()
    time.sleep(time_sync)


