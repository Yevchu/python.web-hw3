import os
import shutil
import argparse
from concurrent.futures import ThreadPoolExecutor

def sort_file(file_path, destination_folder):
    file_name = os.path.basename(file_path)
    name, ext = file_name.split('.')

    destination_path = os.path.join(destination_folder, ext)
    os.makedirs(destination_path, exist_ok=True)

    destination_file_path = os.path.join(destination_path, file_name)
    shutil.move(file_path, destination_file_path)
    print(f"Moved {file_name} to {destination_path}")

def sort_files(source_folder, destination_folder):
    with ThreadPoolExecutor() as executor:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                executor.submit(sort_file, file_path, destination_folder)

def get_folders():

    parser = argparse.ArgumentParser(description='File Sorter')
    parser.add_argument('source_folder', type=str, help='Path to the source folder')
    parser.add_argument('destination_folder', type=str, help='Path to the destination folder')
    args = parser.parse_args()

    source_folder = args.source_folder
    destination_folder = args.destination_folder

    return source_folder, destination_folder

def main():
    source_folder, destination_folder = get_folders()
    sort_files(source_folder, destination_folder)

if __name__ == '__main__':
    main()
    print('You can delete the old folders')






