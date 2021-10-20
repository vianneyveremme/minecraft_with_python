# -*- coding: ascii -*-
from dataclasses import dataclass
import json
import os
import shutil


@dataclass
class Font:
    BOLD = '\033[1m'
    END = '\033[0m'
    ERROR = '\033[91m'
    FINAL_INFO = '\033[94m'
    HEADER = '\033[95m'
    OK_GREEN = '\033[92m'
    UNDERLINE = '\033[4m'
    VARIABLE_INFO = '\033[96m'
    WARN = '\033[93m'

@dataclass
class Minecraft_Pack_Version:
    v1_6_1 = v1_6_2 = v1_6_4 = v1_7_2 = v1_7_4 = v1_7_5 = v1_7_6 = v1_7_8 = v1_7_9 = v1_7_10 = v1_8 = v1_8_1 = v1_8_2 = v1_8_3 = v1_8_4 = v1_8_5 = v1_8_7 = v1_8_8 = v1_8_9 = 1
    v1_9 = v1_9_1 = v1_9_2 = v1_9_3 = v1_9_4 = v1_10 = v1_10_1 = v1_10_2 = 2
    v1_11 = v1_11_1 = v1_11_2 = v1_12 = v1_12_1 = v1_12_2 = 3
    v1_13 = v1_13_1 = v1_13_2 = v1_14 = v1_14_1 = v1_14_2 = v1_14_3 = v1_14_4 = 4
    v1_15 = v1_15_1 = v1_15_2 = v1_16 = v1_16_1 = 5
    v1_16_2 = v1_16_3 = v1_16_4 = v1_16_5 = 6
    v1_17 = v1_17_1 = 7
    LATEST = v1_17_1


def create_file(name, path: str='', content: object='') -> None:
    """
    Create a file with the given name and content.

    :param name: Name of the file to create.
    :param path: Path to the file to create.
    :param content: Content to write to the file.
    """
    with open(f'{path}{os.path.sep}{name}', 'w+', encoding='utf-8') as f:
        if isinstance(content, str):
            f.write(content)
        elif isinstance(content, list):
            for line in content:
                f.write(f'{line}\n')
        elif isinstance(content, dict):
            f.write(json.dumps(content, indent=4, sort_keys=True))
        else:
            raise TypeError(f'Argument "content" must be of type "str" or "list" not {type(content)}!')
        directory_name = f'{path[len(os.getcwd()) + 1:]}{os.path.sep}{Font.END}{name}{Font.OK_GREEN}'
        print(f'{Font.OK_GREEN}Successfuly created the file "{directory_name}".{Font.END}')

def import_from_file(path: str) -> dict | list:
    """
    Import a file from the given path.

    :param path: Path to the file to import.
    :return: The content of the file.
    """
    with open(path, 'r') as f:
        return json.load(f) if path.endswith('.json') else f.readlines()

def make_directory(name: str, path: str='') -> None:
    """
    Create a directory with the given name and path.

    :param name: Name of the directory to create.
    :param path: Path to the directory to create.
    """
    os.mkdir(os.path.join(path, name))
    directory_name = f'{path[len(os.getcwd()) + 1:]}{os.path.sep}{Font.END}{name}{Font.OK_GREEN}'
    print(f'{Font.OK_GREEN}Successfuly created the directory "{directory_name}".{Font.END}')

def remove_directory(path: str='') -> None:
    directory_name = f'{path[len(os.getcwd()) + 1:]}{os.path.sep}{Font.END}{path.split(os.path.sep)[-1]}'
    if os.path.exists(path):
        try:
            shutil.rmtree(path)
            print(f'{Font.FINAL_INFO}Successfuly removed the directory "{directory_name}{Font.FINAL_INFO}".')
        except OSError:
            print(f'{Font.ERROR}Could not remove the directory "{directory_name}{Font.ERROR}".{Font.END}')
    else:
        print(f'{Font.WARN}Directory "{directory_name}".{Font.END}" does not exist!{Font.END}')
