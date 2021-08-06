# -*- coding: ascii -*-
from .utility import create_file, make_directory


class Workspace:
    # TODO: make it printable with __format__.
    def __init__(self, name: str=None) -> None:
        self.name = name if name is not None else 'name'

    def compile(self, path: str) -> None:
        # Create the workspace folder.
        make_directory(self.name, path)
