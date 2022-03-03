# -*- coding: ascii -*-
from datetime import date
from time import time
from typing import Any, Dict, List, Union
from .pack_meta import Pack_Meta
from .workspace import Workspace
from .utility import Minecraft_Pack_Version as MPV
from .utility import Datapack_Replace_Method as DRM
from .utility import Font, Datapack_Namespaces
from .utility import create_file, remove_directory, create_icon_from_string
import os
import shutil


__all__ = ['Datapack']

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
                 pack_mcmeta: Union[Pack_Meta, Dict[str, Any]]=None,
                 workspaces: Union[Workspace, List[Workspace]]=None,
                 auto_compile: bool=None,
                 compile_as_zip: bool=None,
                 replace_existing: bool=None,
                 replace_method: str=None
                 ) -> None:
        """
        Initialize a new Datapack object which will then generate a Minecraft Datapack.

        :param title: The title of the datapack.
        :param path: The path to the datapack.
        :param pack_mcmeta: The metadata of the datapack.
        :param workspaces: The workspace(s) in the datapack.
        :param auto_compile: Whether or not to automatically compile the datapack.
        :param compile_as_zip: Whether or not to compile the datapack as a zip file.
        :param replace_existing: Whether or not to replace an existing datapack with the same name.
        :return: None; this is a constructor.
        """
        self.title = title if title not in (None, '') else "My_Amazing_Datapack"
        self.path = path if path not in (None, '') else os.getcwd()
        self.workspaces = (workspaces if isinstance(workspaces, list) else [workspaces]) if workspaces is not None else []
        self.auto_compile = auto_compile if auto_compile is not None else False
        self.compile_as_zip = compile_as_zip if compile_as_zip is not None else False
        self.replace_existing = replace_existing if replace_existing is not None else False
        self.replace_method = replace_method if replace_method is not None else DRM.DESTROY

        self.pack_mcmeta = pack_mcmeta if pack_mcmeta is not None else Pack_Meta(
            author=f"{os.getlogin()} using MCWPy",
            minecraft_version=MPV.LATEST,
            version=f'{str(date.today().isocalendar()[0])[-2:]}w{date.today().isocalendar()[1]:0>2}s{hex(int(time()))[2:]}'
        )

        # Verifies that the workspaces are valid.
        if not all(isinstance(w, Workspace) for w in self.workspaces):
            raise TypeError(f'{Font.ERROR}The "workspaces" parameter must be a list of Workspace objects.{Font.END}')

        # Auto-compile?
        if self.auto_compile:
            self.compile()

    def __call__(self) -> None:
        self.compile()

    def __format__(self, format_specifier: str=None) -> str:
        """
        Formats the Datapack in a human-readable format depending on the format specifier.
        
        :param format_specifier: The format specifier.
        :return: The formatted string.
        """
        return f"{self.__str__():{format_specifier}}"

    def __getitem__(self, index: int) -> Workspace:
        """
        Return the Workspace at the given index.

        :param index: The index of the Workspace to return.
        :return: The Workspace at the given index.
        """
        return self.workspaces[index]

    def __len__(self) -> int:
        """Return the number of Workspaces in the Datapack."""
        return len(self.workspaces)

    def __repr__(self) -> str:
        """Return a string representation of the Datapack."""
        return f"{self.title}: {self.workspaces}"

    def __str__(self) -> str:
        """Return a string representation of the Datapack."""
        return self.__repr__()

    def append(self, element: object) -> None:
        """
        Add a Workspace or a list of Workpaces to the Datapack.

        :param element: The Workspace or the list of Workspaces to add to the Datapack.
        """
        if isinstance(element, Workspace):
            self.workspaces.append(element)
        elif isinstance(element, list | Workspace):
            for e in element:
                self.append(e)
        else:
            raise TypeError(f'{Font.ERROR}The "element" parameter must be a Workspace or a list of Workspaces.{Font.END}')

    def compile(self) -> None:
        """
        Compiles the data entered by the user to create a Minecraft Datapack.

        :return: None; this is a builder function (builds files).
        """
        if os.path.exists(os.path.join(self.path, self.title)):
            if self.replace_existing or input(f'{Font.WARN}{self.title} already exists, do you want to replace it? [yes/no]: {Font.END}')[0].lower() == 'y':
                match self.replace_method:
                    case DRM.DESTROY:
                        remove_directory(os.path.join(self.path, self.title))
                    case DRM.KEEP:
                        raise TypeError(f'{Font.ERROR}Replace method not implemented yet.{Font.END}')
                    case DRM.REPLACE:
                        raise TypeError(f'{Font.ERROR}Replace method not implemented yet.{Font.END}')
                    case _:
                        if any(
                            self.replace_method == getattr(Datapack_Namespaces, namespace)
                            for namespace in [e for e in dir(Datapack_Namespaces) if not '_' in e]
                        ):
                            raise TypeError(f'{Font.ERROR}Replace method not implemented yet.{Font.END}')
                        else:
                            raise TypeError(f'{Font.ERROR}Wrong replace method.{Font.END}')
            else:
                raise FileExistsError(f'{Font.ERROR}{self.title} already exists, and you have not chosen to replace it.{Font.END}')

        # Create the pack.mcmeta and pack.png files.
        create_file('pack.mcmeta', os.path.join(self.path, self.title), self.pack_mcmeta() if isinstance(self.pack_mcmeta, Pack_Meta) else self.pack_mcmeta)
        create_icon_from_string(self.title, os.path.join(self.path, self.title, 'pack.png'))

        # Compile every workspace in the Datapack.
        for w in self.workspaces:
            w.compile(os.path.join(self.path, self.title, 'data'))

        ########################
        # AT THE END
        ########################
        # Zip the Datapack.
        if self.compile_as_zip:
            self.to_zip()

    def pop(self, index: int=-1) -> Workspace:
        """
        Remove and return the Workspace at the given index.

        :param index: The index of the Workspace to remove.
        :return: The Workspace removed.
        """
        return self.workspaces.pop(index)

    def to_zip(self) -> None:
        """This function compresses the Datapack into a zip file."""
        if os.path.exists(os.path.join(self.path, self.title + '.zip')):
            if self.replace_existing or input(f'{Font.WARN}{self.title}.zip already exists, do you want to replace it? [yes/no]: {Font.END}')[0].lower() == 'y':
                os.remove(os.path.join(self.path, self.title + '.zip'))
            else:
                raise FileExistsError(f'{Font.ERROR}{self.title}.zip already exists, and you have not chosen to replace it.{Font.END}')

        # Actually create the zip file.
        shutil.make_archive(self.title, 'zip', os.path.join(self.path, self.title))
        
        if os.path.exists(os.path.join(self.path, self.title + '.zip')):
            print(f'{Font.OK_GREEN}Successfuly created the archive "{self.title}.zip".{Font.END}')

            # Remove the original files
            if os.path.exists(os.path.join(self.path, self.title)):
                remove_directory(os.path.join(self.path, self.title))
        else:
            # Print an error message and say the original file was saved.
            print(f'{Font.ERROR}Failed to create the file "{self.title}.zip".{Font.END}', f'{Font.FINAL_INFO}The file {self.title} was not deleted.{Font.END}')
