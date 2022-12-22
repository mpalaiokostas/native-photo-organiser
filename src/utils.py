import json
import pathlib

def read_user_input(filename):
    with open(filename) as json_file:
        user_input = json.load(json_file)
    return user_input


def parse_str_to_directory(str_dir):
    return None