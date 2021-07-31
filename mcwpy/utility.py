import json
import os


class Font:
    BOLD = '\033[1m'
    END = '\033[0m'
    FAIL = KO_RED = '\033[91m'
    FINAL_INFO_BLUE = '\033[94m'
    HEADER = '\033[95m'
    INFO_CYAN = '\033[96m'
    OK_GREEN = '\033[92m'
    UNDERLINE = '\033[4m'
    WARNING = '\033[93m'


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
            for line in str(content).replace("'", '"').lower():
                f.write(f'{line}')
        else:
            raise TypeError(f'Argument "content" must be of type "str" or "list" not {type(content)}!')
        print(f'Successfuly created the file "{name}".')

def make_directory(name: str, path: str='') -> None:
    """
    Create a directory with the given name and path.

    :param name: Name of the directory to create.
    :param path: Path to the directory to create.
    """
    os.mkdir(f'{path}{os.path.sep}{name}')
    print(f'Successfuly created the directory "{name}".')
