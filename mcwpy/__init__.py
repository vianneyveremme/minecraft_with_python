# -*- coding: utf-8 -*-
""" MCWPy - Minecraft With Python

MCWPy is a Python library for creating Minecraft datapacks using Python.
    https://github.com/vianneyveremme/minecraft_with_python
"""
from .datapack import Datapack
from .workspace import Workspace
from .utility import Font
import sys


# Checking Python version (should be above 3.9.5)
if sys.version_info < (3, 9, 5):
    print(f"{Font.WARNING}For optimal results it is recommended to use Python 3.9.5 or above.{Font.END}")
else:
    print(f"{Font.HEADER}{Font.BOLD}Hello from the MCWPy community :){Font.END}")

# Print the location where the default path is
print(f"{Font.INFO_CYAN}Default path: {Datapack().path}.{Font.END}")
