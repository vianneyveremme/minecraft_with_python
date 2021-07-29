# -*- coding: utf-8 -*-
from datetime import date
from time import time
import os


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
        self.workspaces = workspaces if workspaces is not None else []
        self.auto_compile = auto_compile if auto_compile is not None else False
        self.compile_as_zip = compile_as_zip if compile_as_zip is not None else False
        self.replace_existing = replace_existing if replace_existing is not None else False
        self.description = description if description is not None else ""
        self.version = version if version is not None else f'{str(date.today().isocalendar()[0])[-2:]}w{date.today().isocalendar()[1]}s{int(time())}'
