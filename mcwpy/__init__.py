# -*- coding: ascii -*-
""" MCWPy - Minecraft With Python

MCWPy is a Python library for creating Minecraft datapacks using Python.
    https://github.com/vianneyveremme/minecraft_with_python
"""
from .datapack import Datapack
from .workspace import Workspace
from .utility import Font, Minecraft_Pack_Version
from .pack_meta import Pack_Meta
import sys


# Checking Python version (should be above 3.9.5)
if sys.version_info < (3, 9, 5):
    print(f"{Font.WARN}For optimal results it is recommended to use Python 3.9.5 or above.{Font.END}")
else:
    print(f"{Font.HEADER}{Font.BOLD}Hello from the MCWPy community :){Font.END}")

# Print the location where the default path is
print(f"{Font.VARIABLE_INFO}Default path: {Datapack().path}.{Font.END}")
