# -*- coding: ascii -*-
from .utility import create_file, Font, make_directory, remove_directory
import json
import os
import random
import string

class Workspace:
    """
    Workspaces are the directories that contain the code and data files.
    """
    # TODO: make it printable with __format__.
    def __init__(self, name: str=None, **kwargs) -> None:
        """
        Initialize a workspace.
        
        :param name: The name of the workspace.
        :param kwargs: The content of the workspace.
        """
        self.name = name.lower() if name is not None else f"workspace_{''.join([random.choice(string.ascii_lowercase + string.digits) for _ in range(8)])}"
        self.arguments = kwargs if len(kwargs) > 0 else {}

        self.possible_arguments = {
            'advancements', 'dimension', 'dimension_type', 'functions', 'item_modifiers', 
            'loot_tables', 'predicates', 'recipes', 'structures', 'tags', 'worldgen'
        }
        
    def compile(self, path: str, as_subfolder: bool=False) -> None:
        # Create the workspace folder.
        make_directory(self.name, path)

        # Difference between "main Workspace" and "sub Workspace".
        _as_subfolder = as_subfolder if as_subfolder is not None else False

        # Create the workspace files.
        for key_word in self.arguments:
            if not _as_subfolder:
                make_directory(key_word, os.path.join(path, self.name))
            
            for key in self.arguments[key_word]:
                if isinstance(self.arguments[key_word][key], str):
                    create_file(
                        f'{key}.' + ('mcfunction' if key_word == 'functions' else 'json') if key_word in self.possible_arguments else key,
                        os.path.join(path, self.name, '' if _as_subfolder else key_word), self.arguments[key_word][key]
                    )
                elif isinstance(self.arguments[key_word][key], list | set):
                    create_file(
                        f'{key}.' + ('mcfunction' if key_word == 'functions' else 'json') if key_word in self.possible_arguments else key,
                        os.path.join(path, self.name, '' if _as_subfolder else key_word), '\n'.join(self.arguments[key_word][key])
                    )
                elif isinstance(self.arguments[key_word][key], Workspace):
                    self.arguments[key_word][key].compile(os.path.join(path, self.name, key_word), as_subfolder=True)
                else:
                    print('dunno')
