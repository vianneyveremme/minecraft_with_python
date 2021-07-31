# -*- coding: utf-8 -*-
from datetime import date
from time import time
from .workspace import Workspace
import os
import shutil


class Datapack:
    """
    Datapacks can be placed in the .minecraft/saves/(world)/datapacks folder of a world. Each data pack is either a sub-folder or a .zip file \
        within the datapacks folder. After it is in the folder, a data pack is enabled for that world when the world is reloaded or loaded.
    Data packs load their data based on the load order. This order can be seen and altered by using the /datapack command and is stored in the \
        level.dat file.

    The player can also select data packs at the world creation screen by clicking the Data Packs button and dragging-and-dropping their data \
        pack folders/zip-files there. This is similar to the Resource Pack selection screen, and allows the player to enable data packs before \
        the world is generated, and easily customize the load order too.
    """
    def __init__(self, 
                 title: str=None,
                 path: str=None,
                 author: str=None,
                 pack_mcmeta: dict=None,
                 workspaces: list=None,
                 auto_compile: bool=None,
                 compile_as_zip: bool=None,
                 replace_existing: bool=None,
                 description: str=None,
                 version: str=None
                 ) -> None:
        """
        Initialize a new Datapack object which will then generate a Minecraft Datapack.

        :param title: The title of the datapack.
        :param path: The path to the datapack.
        :param author: The author of the datapack.
        :param pack_mcmeta: The metadata of the datapack.
        :param workspaces: The workspace(s) in the datapack.
        :param auto_compile: Whether or not to automatically compile the datapack.
        :param compile_as_zip: Whether or not to compile the datapack as a zip file.
        :param replace_existing: Whether or not to replace an existing datapack with the same name.
        :param description: A short description of the datapack.
        :param version: The version of the datapack.
        :return: None; this is a constructor.
        """
        self.title = title if title not in [None, ''] else "My_Amazing_Datapack"
        self.path = path if path is not None else os.getcwd()
        self.author = author if author is not None else "MCWPy"
        self.pack_mcmeta = pack_mcmeta if pack_mcmeta is not None else {}
        self.workspaces = (workspaces if isinstance(workspaces, list) else [workspaces]) if workspaces is not None else []
        self.auto_compile = auto_compile if auto_compile is not None else False
        self.compile_as_zip = compile_as_zip if compile_as_zip is not None else False
        self.replace_existing = replace_existing if replace_existing is not None else False
        self.description = description if description is not None else ""
        self.version = version if version is not None else f'{str(date.today().isocalendar()[0])[-2:]}w{date.today().isocalendar()[1]}s{int(time())}'

        # Verifies that the path is a valid datapack path
        self._exists = os.path.exists(self.path + self.title)

        if self._exists and not self.replace_existing:
            self.replace_existing = input(f'{self.title} already exists, do you want to replace it? [yes/no]: ')[0].lower() == 'y'

            if not self.replace_existing:
                raise FileExistsError(f'The datapack "{self.title}" already exists. Please specify a new name or set the "replace_existing" parameter to True.')

        # Verifies that the workspaces are valid.
        if not all(isinstance(w, Workspace) for w in self.workspaces):
            raise TypeError(f'The "workspaces" parameter must be a list of Workspace objects.')

        # Auto-compile?
        if self.auto_compile:
            self.compile()

    def __getitem__(self, index: int) -> Workspace:
        """
        Select the workspace at the given index.

        :param index: The index of the workspace to select.
        :return: The selected workspace.
        """
        return self.workspaces[index]

    def __iter__(self) -> iter:
        """Return an iterator over the workspaces in the Datapack."""
        return Datapack_Iterator(self.workspaces)

    def __len__(self) -> int:
        """Return the number of workspaces in the Datapack."""
        return len(self.workspaces)

    def __repr__(self) -> str:
        """Return a string representation of the Datapack."""
        return self.__str__()

    def __reversed__(self) -> None:
        """Return an iterator over the workspaces in the Datapack in reverse order."""
        return Datapack_Iterator(self.workspaces)[::-1]

    def __str__(self) -> str:
        """Return a string representation of the Datapack."""
        return "---- {}\n\t|\n\t---- pack.mcmeta: {}\n\t---- pack.png\n\t---- data\n\t\t|\n\t\t{}".format(
            self.title, self.pack_mcmeta, ', \n\t\t'.join(map(lambda x: f'---- {x.name}', self.workspaces))
        )

    def append(self, element: object) -> None:
        """
        Add a Workspace or a list of Workpaces to the Datapack.

        :param element: The Workspace or the list of Workspaces to add to the Datapack.
        """
        if isinstance(element, Workspace):
            self.workspaces.append(element)
        elif isinstance(element, list):
            for e in element:
                self.append(e)

    def pop(self, index: int=-1) -> Workspace:
        """
        Remove and return the Workspace at the given index.

        :param index: The index of the Workspace to remove.
        :return: The Workspace removed.
        """
        return self.workspaces.pop(index)

    def compile(self) -> None:
        """
        Compiles the data entered by the user to create a Minecraft Datapack.

        :return: None; this is a builder function (builds files).
        """
        if self._exists:
            if self.replace_existing:
                shutil.rmtree(self.path + os.path.sep + self.title)
            else:
                raise FileExistsError(f'The datapack "{self.title}" already exists. Please specify a new name or set the "replace_existing" parameter to True.')

class Datapack_Iterator:
    """Iterator class for Datapack"""
    def __init__(self, workspaces) -> None:
        """
        Initialize a new Datapack_Iterator object which will iterate over the workspaces in a Datapack.

        :param workspaces: The list of workspaces to iterate through.
        """
        self._workspaces = workspaces
        self._index = 0

    def __next__(self) -> Workspace:
        """Select the next workspace in the Datapack until the end is reached."""
        if self._index < len(self._workspaces):
            result = self._workspaces[self._index]
            self._index += 1
            return result
        raise StopIteration
