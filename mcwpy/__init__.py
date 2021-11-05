# -*- coding: ascii -*-
""" 
 __  __  _______          _______       
|  \/  |/ ____\ \        / /  __ \      
| \  / | |     \ \  /\  / /| |__) |   _ 
| |\/| | |      \ \/  \/ / |  ___/ | | |
| |  | | |____   \  /\  /  | |   | |_| |
|_|  |_|\_____|   \/  \/   |_|    \__, |
                                   __/ |
                                  |___/ 

Minecraft with Python is a Python library for creating Minecraft datapacks using Python.
    https://github.com/vianneyveremme/minecraft_with_python
"""
from .datapack import Datapack
from .workspace import Workspace
from .utility import Font, Minecraft_Pack_Version
from .pack_meta import Pack_Meta
import sys


# Checking Python version (should be above 3.10.0)
if sys.version_info < (3, 10, 0):
    print(f"{Font.WARN}For optimal results it is recommended to use Python 3.10.0 or above.{Font.END}")
else:
    print(f"{Font.HEADER}{Font.BOLD}Hello from the MCWPy community :){Font.END}")
del sys

# Print the location where the default path is
print(f"{Font.VARIABLE_INFO}Default path: {Datapack().path}.{Font.END}")
