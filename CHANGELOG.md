# 0.0.12 ()
+ Added a check to verify whether the Minecraft Workspace can be automatically created.  
+ Added a function to remove directories.  
+ Added `utility.py` to the library for tools that can be useful for other modules.  
+ Added `__format__` representation for Datapack objects.  
+ Made the Datapack compilation delete the old Datapack folder if authorized.  
+ Made the library inform the user where the Datapack folder by default is.  
* Changed `ansi_escape_sequence.py` into `utility.py`.  
* Changed code encryption from `utf-8` to `ascii`.  
* Changed the way the Datapack folder is ziped.  
* Changed replacement of older versions of the Datapack folder.  
* Changed the Font class to a dataclass.  
* Updated the `.gitignore` file to ignore the generated test files.  
- Removed unused import in `datapack.py`.  

# 0.0.11 (2021/07/30)
+ Added many more tests to `datapack.py`.  
+ Made Datapacks iterable by going through their Workspaces.  
* Updated `CHANGELOG.md` way of displaying additions *(`+`)*, changes *(`*`)* and removals *(`-`)*.  
* Updated the way to do the tests.  

# 0.0.10 [0.0.9, 0.0.8] (2021/07/30)
* Fixed library import issues - `datapack.py` was not importing `workspace.py` with relative imports.  

# 0.0.7 (2021/07/30)
+ Added `requests==2.26.0` to `REQUIREMENTS.txt`.  
+ Added `tests.py` in which unit tests are and will be written.  
+ Added `workspace.py` to create the class `Workspace` which handles the `Datapack` workspaces.  
+ Wrote several tests for the `Datapack` class (`datapack.py`).  
* Improved the `README.md`.  
* Improved the `Datapack`'s `workspaces` default attribute.  
- Removed `test.py`.  

# 0.0.6 (2021/07/29)
+ Now printing the library version when imported.  
* Fixed version **0.0.5** by using relative imports.  

# 0.0.5 (2021/07/29)
* Fixed version **0.0.4** by removing inputs in `setup.py`.  
* Updated `verify_setup.py` to check if the display format is correct.  

# 0.0.4 (2021/07/29)
+ Added ANSI escape sequences to the output for prettier messages (`ansi_escape_sequences.py`).  
+ Added an automatic version code for Datapacks with unspecified versions.  
+ Added `verify_setup.py` to check if the package can be created.  
* Changed warnings to be easier to read.  
* Version **0.0.3** did not work so MCWPy will be developed without subfolders.  

# 0.0.3 (2021/07/29)
* Attempt to use subfolders...  
* If creating a Datapack using the MCWPy library works then it is a success.  

# 0.0.2 (2021/07/28)
+ Made the library check if is running on [Python](https://www.python.org/downloads/) **3.9.5** or above.  

# 0.0.1 (2021/07/28)
* Fixed (or tried to) `CHANGELOG.md`, `LICENSE` and `README.md` looks on [pypi.org](https://pypi.org/project/mcwpy/).  

# Initial (2021/07/28)
+ Created a `setup.py` file to setup the library.  
+ Created two functions to add or substract numbers together.  
+ Created `mcwpy\__init__.py`.  
+ Created `REQUIREMENTS.txt`.  
+ Wrote `LICENSE`.  
+ Wrote `MANIFEST.md`.  
+ Wrote `README.md`.  
* Used `python3 setup.py sdist` in a terminal to create the library's first package.  
* Used `twine upload --repository-url https://upload.pypi.org/legacy/ dist/*` to upload the library's first package on pypi.  
