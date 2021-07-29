# -*- coding: utf-8 -*-
""" MCWPy - Minecraft With Python

MCWPy is a Python library for creating Minecraft datapacks using Python.
    https://github.com/vianneyveremme/minecraft_with_python
"""
from .ansi_escape_sequences import Font
from .datapack import Datapack
from .test import *
import sys


# Checking Python version (should be above 3.9.5)
if sys.version_info < (3, 9, 5):
    print(f"{Font.WARNING}For optimal results it is recommended to use Python 3.9.5 or above.{Font.ENDC}")
else:
    print(f"{Font.HEADER}{Font.BOLD}Hello from the MCWPy community :){Font.ENDC}")
