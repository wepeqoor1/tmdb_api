import json
import os

def load_data(path):
    if not os.path.exists(path):
        return None
    with open(path, mode='r', encoding='utf-8') as my_file:
        return json.load(my_file)
