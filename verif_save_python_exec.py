import subprocess
import os
import json
import time

def get_file_size(file_path):
    try:
        file_stats = os.stat(file_path)
        return file_stats.st_size
    except FileNotFoundError:
        print(f"Le fichier '{file_path}' n'existe pas.")
        return None

def write_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=True, indent=4)

def read_json(file):
    try:
        with open(file, "r", encoding="utf-8") as file:
            data = json.load(file)
    except:
        data = {}
    return data

def check_and_copy_files():
    while True:
        data = read_json("data_file.json")
        command = "find folder/to/verification -type f -name '*.py'"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
        files = result.stdout.splitlines()
        times = [round(get_file_size(x)) for x in files]
        dictio = dict(zip(files, times))

        if not os.path.exists("save_folder"):
            os.mkdir("save_folder")

        for key, value in dictio.items():
            if key not in data or value != data[key]:
                os.system(f"cp {key} save_folder")

        write_json(dictio, "data_file.json")
        time.sleep(1)  # Wait for an hour before checking again

if __name__ == "__main__":
    check_and_copy_files()
