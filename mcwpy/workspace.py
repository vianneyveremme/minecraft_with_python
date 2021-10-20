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
    def __init__(self, name: str=None, **content) -> None:
        """
        Initialize a workspace.
        
        :param name: The name of the workspace.
        :param content: The content of the workspace.
        """
        self.name = name.lower() if name is not None else f"workspace_{''.join([random.choice(string.ascii_lowercase + string.digits) for _ in range(8)])}"
        self.content = content if len(content) > 0 else {}

        self.possible_arguments = {
            'advancements', 'dimension', 'dimension_type', 'functions', 'item_modifiers', 
            'loot_tables', 'predicates', 'recipes', 'structures', 'tags', 'worldgen'
        }

    def __repr__(self) -> str:
        # print the workspace with each of its arguments and arguments content.
        return "---- {}\n\t|\n\t---- {}\n\t\t|\n\t\t{}".format(
            self.name, ''.join(map(lambda x: x, self.content)),
            ''.join(map(lambda x: json.dumps(self.content[x]), self.content))
        )

    def __str__(self) -> str:
        return self.__repr__()

    def compile(self, path: str, as_subfolder: bool=False) -> None:
        # Create the workspace folder.
        make_directory(self.name, path)

        # Difference between "main Workspace" and "sub Workspace".
        _as_subfolder = as_subfolder if as_subfolder is not None else False

        # Create the workspace files.
        for key_word in self.content:
            if not _as_subfolder:
                make_directory(key_word, os.path.join(path, self.name))
            
            for key in self.content[key_word]:
                if isinstance(key, str):
                    create_file(
                        f'{key}.' + ('mcfunction' if key_word == 'functions' else 'json') if key_word in self.possible_arguments else key,
                        os.path.join(path, self.name, '' if _as_subfolder else key_word), self.content[key_word][key]
                    )
                elif isinstance(key, list):
                    create_file(
                        f'{key}.' + ('mcfunction' if key_word == 'functions' else 'json') if key_word in self.possible_arguments else key,
                        os.path.join(path, self.name, '' if _as_subfolder else key_word), '\n'.join(self.content[key_word][key])
                    )
                elif isinstance(key, dict):
                    for sub_key in key.keys():
                        create_file(
                            f'{sub_key}.' + ('mcfunction' if key_word == 'functions' else 'json') if key_word in self.possible_arguments else sub_key,
                            os.path.join(path, self.name, '' if _as_subfolder else key_word), key[sub_key]
                        )
                elif isinstance(key, Workspace):
                    key.compile(os.path.join(path, self.name, key_word if not _as_subfolder else ''), as_subfolder=True)
                
                # Load and tick JSONs
                if key_word == 'functions':
                    def create_tick_load(filename:str):
                        if not os.path.exists(os.path.join(path, 'minecraft', 'tags')):
                            make_directory('tags', os.path.join(path, 'minecraft'))

                        if not os.path.exists(os.path.join(path, 'minecraft', 'tags', 'functions')):
                            make_directory('functions', os.path.join(path, 'minecraft', 'tags'))

                        if os.path.exists(os.path.join(path, 'minecraft', 'tags', 'functions', filename.replace('main', 'tick'))):
                            with open(os.path.join(path, 'minecraft', 'tags', 'functions', filename.replace('main', 'tick')), 'r') as f:
                                data = json.load(f)
                                data['values'].append(f"{self.name}:{filename.removesuffix('.json')}")
                            with open(os.path.join(path, 'minecraft', 'tags', 'functions', filename.replace('main', 'tick')), 'w') as f:
                                f.write(json.dumps(data, indent=4))
                        else:
                            create_file(filename.replace('main', 'tick'), os.path.join(path, 'minecraft', 'tags', 'functions'), 
                                content=json.dumps({"values": [f"{self.name}:{filename.removesuffix('.json')}"]}, indent=4))

                    if isinstance(key, dict):
                        for sub_key in key.keys():
                            if sub_key in ['load', 'main', 'tick']:
                                create_tick_load(f"{sub_key}.json")

                if key in ['load', 'main', 'tick']:
                    create_tick_load(f"{key}.json")
