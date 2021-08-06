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


def create_file(name, path: str='', content: object='') -> None:
    """
    Create a file with the given name and content.

    :param name: Name of the file to create.
    :param path: Path to the file to create.
    :param content: Content to write to the file.
    """
    with open(f'{path}{os.path.sep}{name}', 'w+') as f:
        if isinstance(content, str):
            f.write(content)
        elif isinstance(content, list):
            for line in content:
                f.write(f'{line}\n')
        elif isinstance(content, dict):
            json.dumps(content, indent=4, sort_keys=True)
        else:
            raise TypeError(f'Argument "content" must be of type "str" or "list" not {type(content)}!')
        print(f'{Font.OK_GREEN}Successfuly created the file "{name}".{Font.END}')

def make_directory(name: str, path: str='') -> None:
    """
    Create a directory with the given name and path.

    :param name: Name of the directory to create.
    :param path: Path to the directory to create.
    """
    os.mkdir(os.path.join(path, name))
    print(f'{Font.OK_GREEN}Successfuly created the directory "{name}".{Font.END}')

def remove_directory(name: str, path: str='') -> None:
    if os.path.exists(f'{os.path.join(path, name)}'):
        try:
            shutil.rmtree(os.path.join(path, name))
            print(f'{Font.FINAL_INFO}Successfuly removed the directory "{name}".{Font.END}')
        except OSError:
            print(f'{Font.ERROR}Could not remove the directory "{name}".{Font.END}')
    else:
        print(f'{Font.WARN}Directory "{name}" does not exist!{Font.END}')
