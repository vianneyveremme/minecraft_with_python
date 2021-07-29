# 0.0.7 ()
- ...

# 0.0.6 (2021/07/29)
- Fixed version **0.0.5** by using relative imports.  
- Printing the library version when imported.  

# 0.0.5 (2021/07/29)
- Fixed version **0.0.4** by removing inputs in `setup.py`.  
- Updated `verify_setup.py` to check if the display format is correct.  

# 0.0.4 (2021/07/29)
- Added ANSI escape sequences to the output for prettier messages (`ansi_escape_sequences.py`).  
- Added an automatic version code for Datapacks with unspecified versions.  
- Added `verify_setup.py` to check if the package can be created.  
- Changed warnings to be easier to read.  
- Version **0.0.3** did not work so MCWPy will be developed without subfolders.  

# 0.0.3 (2021/07/29)
- Attempt to use subfolders...  
- If creating a Datapack using the MCWPy library works then it is a success.  

# 0.0.2 (2021/07/28)
- Made the library check it is running on [Python](https://www.python.org/downloads/) **3.9.5** or above.  

# 0.0.1 (2021/07/28)
- Fixed (or tried to) `CHANGELOG.md`, `LICENSE` and `README.md` looks on [pypi.org](https://pypi.org/project/mcwpy/).  

# Initial (2021/07/28)
- Created a `setup.py` file to setup the library.  
- Created two functions to add or substract numbers together.  
- Created `mcwpy\__init__.py`.  
- Created `REQUIREMENTS.txt`.  
- Used `python3 setup.py sdist` in a terminal to create the library's first package.  
- Used `twine upload --repository-url https://upload.pypi.org/legacy/ dist/*` to upload the library's first package on pypi.  
- Wrote `LICENSE`.  
- Wrote `MANIFEST.md`.  
- Wrote `README.md`.  
