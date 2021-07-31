# -*- coding: utf-8 -*-
class Workspace:
    # TODO: make it printable with __format__
    def __init__(self, name:str=None) -> None:
        self.name = name if name is not None else 'name'
