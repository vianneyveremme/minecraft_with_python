# -*- coding: ascii -*-
import json
from .utility import Minecraft_Pack_Version


__all__ = ['Pack_Meta']

class Pack_Meta:
    def __init__(self, author: str=None, description: str=None, minecraft_version: object=None, **kwargs) -> None:
        """
        Create a new pack.mcmeta object to transform into a json string.

        :param author: The author of the datapack.
        :param description: A short description of the datapack.
        :param minecraft_version: The Minecraft version used to select appropriate pack format.
        """
        self.meta = dict()

        if isinstance(author, str) and len(author) > 0:
            self.meta['author'] = author

        self.meta['description'] = description if isinstance(description, str) and len(description) > 0 else 'A Minecraft datapack.'
        self.meta['pack_format'] = minecraft_version if isinstance(minecraft_version, Minecraft_Pack_Version) else Minecraft_Pack_Version.LATEST

        for key, value in kwargs.items():
            self.meta[key] = value

    def __call__(self) -> str:
        """Return the json string of the pack.mcmeta object."""
        return json.dumps({'pack': self.meta}, indent=4)

    def __repr__(self) -> str:
        """Return the json string of the pack.mcmeta object."""
        return self.__call__()

    def __str__(self) -> str:
        """Return the json string of the pack.mcmeta object."""
        return self.__call__()
