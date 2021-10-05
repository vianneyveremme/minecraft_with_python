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
    def __init__(self, name: str=None, content: dict=None, workspaces: dict=None) -> None:
        """
        Initialize a workspace.
        
        :param name: The name of the workspace.
        :param content: The content of the workspace.
        :param workspaces: The workspaces that are contained in this workspace (subfolders).
        :return: None, this is a constructor.
        """
        self.name = name if name is not None else f"workspace_{''.join([random.choice(string.ascii_letters + string.digits) for _ in range(8)])}"
        self.content = content if content is not None else {}
        self.workspaces = workspaces if workspaces is not None else {}
        
        # Verifies that the workspaces are valid.
        if not all(isinstance(w, Workspace) for w in self.workspaces):
            raise TypeError(f'{Font.ERROR}The "workspaces" parameter must be a list of Workspace objects.{Font.END}')

    def compile(self, path: str, as_subfolder: bool=False) -> None:
        # Create the workspace folder.
        make_directory(self.name, path)

        # Difference between "main Workspace" and "sub Workspace".
        _as_subfolder = as_subfolder if as_subfolder is not None else False

        folder = 'functions'
        # Create the workspace files.
        if _as_subfolder:
            for file_name in self.content:
                create_file(f'{file_name}.mcfunction', os.path.join(path, self.name), self.content[file_name])
        else:
            for file_type in self.content:
                if any(file_type == e or file_type + 's' == e for e in [
                    'advancement', 'function', 'item_modifier', 'loot_table', 'predicate',
                    'recipe', 'structure', 'tag', 'dimension', 'dimension_type', 'worldgen'
                ]):
                    folder = file_type if file_type[-1] == 's' else file_type + 's'

                make_directory(folder, os.path.join(path, self.name))
                for file_name in self.content[file_type]:
                    create_file(
                        f'{file_name}.mcfunction' if 'fun' in file_type else f'{file_name}.json',
                        os.path.join(path, self.name, folder), self.content[file_type][file_name]
                    )

                    # Load and Tick minecraft files.
                    if file_name in ('load', 'load.mcfunction', 'main', 'main.mcfunction', 'tick', 'tick.mcfunction'):
                        if not os.path.exists(os.path.join(path, 'minecraft', 'tags')):
                            make_directory('tags', os.path.join(path, 'minecraft'))

                        if not os.path.exists(os.path.join(path, 'minecraft', 'tags', 'functions')):
                            make_directory('functions', os.path.join(path, 'minecraft', 'tags'))

                        if 'load' in file_name:
                            if os.path.exists(os.path.join(path, 'minecraft', 'tags', 'functions', 'load')):
                                ...
                            else:
                                create_file('load.json', os.path.join(path, 'minecraft', 'tags', 'functions'), content=json.dumps({"values":[f"{self.name}:load"]}, indent=4))

                        if 'main' in file_name:
                            if os.path.exists(os.path.join(path, 'minecraft', 'tags', 'functions', 'tick')):
                                ...
                            else:
                                create_file('tick.json', os.path.join(path, 'minecraft', 'tags', 'functions'), content=json.dumps({"values":[f"{self.name}:main"]}, indent=4))

                        if 'tick' in file_name:
                            if os.path.exists(os.path.join(path, 'minecraft', 'tags', 'functions', 'tick')):
                                ...
                            else:
                                create_file('tick.json', os.path.join(path, 'minecraft', 'tags', 'functions'), content=json.dumps({"values":[f"{self.name}:tick"]}, indent=4))

        for w in self.workspaces:
            w.compile(os.path.join(path, self.name, folder), as_subfolder=True)
