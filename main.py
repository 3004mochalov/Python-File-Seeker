import os
import shutil


def copy_python_files(source_folder, target_folder, log_name):
    total_bytes = 0
    if os.path.abspath(source_folder) == os.path.abspath(target_folder):
        raise ValueError("Source and target folders are the same")

    with open(log_name, "w", encoding="utf-8") as log_file:
        log_file.write("Имя файла (|||||||) Прежняя директория\n")
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if file.endswith(".py"):
                    source_path = os.path.join(root, file)
                    target_path = os.path.join(target_folder, file)
                    if os.path.abspath(source_path) != os.path.abspath(target_path):
                        shutil.copy2(source_path, target_path)
                        log_file.write(f"{file}, (|||||||) ,{source_path}\n")
                        total_bytes += os.path.getsize(target_path)

    print("Копирование и вставка файлов завершены.")
    print("Информация о количестве записанных данных:")
    print(f"Байты: {total_bytes}")
    print(f"Килобайты: {total_bytes / 1024}")
    print(f"Мегабайты: {total_bytes / (1024 * 1024)}")

# Пример использования
source_folder = "С:\\"  # Укажите путь к исходной папке
target_folder = "E:\\всеКоды"  # Укажите путь к целевой папке
log_name = "log.txt"

confirm = input(
    "Внимание! Копирование и вставка файлов может привести к износу ячеек SSD. Хотите продолжить? (y/n): ")
if confirm.lower() == "y":
    copy_python_files(source_folder, target_folder, log_name)
else:
    print("Операция отменена.")

#source_folder = "H:\\"  # Укажите путь к исходной папке
#target_folder = "E:\\всеКоды2"  # Укажите путь к целевой папке
#log_name = "log1.txt"

#if confirm.lower() == "y":
#    copy_python_files(source_folder, target_folder, log_name)
#else:
#    print("")


exitMessage = input(
    "Нажмите enter чтобы закрыть программу")