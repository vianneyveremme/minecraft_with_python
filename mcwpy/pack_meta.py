# -*- coding: ascii -*-
import json
from .utility import Minecraft_Pack_Version


class Pack_Meta:
    def __init__(self, author: str=None, description: str=None, minecraft_version: object=None) -> None:
        self.meta = dict()

        if len(author) > 0 and isinstance(author, str):
            self.meta['author'] = author
        
        if len(description) > 0:
            self.meta['description'] = description if isinstance(description, str) else description.join('\n')

        self.meta['pack_format'] = minecraft_version if isinstance(minecraft_version, Minecraft_Pack_Version) else Minecraft_Pack_Version.LATEST

    def __repr__(self) -> str:
        return json.dumps({'pack': self.meta}, indent=4)
