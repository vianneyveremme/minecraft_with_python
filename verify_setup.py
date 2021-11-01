# -*- coding: ascii -*-
from datetime import date
from _version import __version__
import requests


class Font:
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'


def version_to_tuple(version:str) -> tuple:
    return tuple(map(int, version.split('.')))


# Get the latest released version of the package
try:
    data = requests.get('https://pypi.org/pypi/mcwpy/json').json()
except Exception as e:
    print(f'{Font.FAIL}Unable to resolve latest release version: "{e}"{Font.END}')
    quit()
except BaseException:
    print(f'{Font.FAIL}Unable to resolve latest release version.{Font.END}')
    quit()
else:
    print(f'{Font.OK_GREEN}Latest released version: {data["info"]["version"]}.{Font.END}')
del requests

# Verify that the version is the latest
if version_to_tuple(data['info']['version']) < version_to_tuple(__version__):
    print(f'{Font.OK_GREEN}New version: {__version__}.{Font.END}')
else:
    print(f"{Font.FAIL}New version ({__version__}) <= older version ({data['info']['version']}).{Font.END}")
    quit()

# Verify that the CHANGELOG is up to date
if f"# {__version__} ({str(date.today()).replace('-', '/')})" in open('CHANGELOG.md').read():
    print(f'{Font.OK_GREEN}CHANGELOG.md is up to date.{Font.END}')
else:
    print(f'{Font.FAIL}Unable to read CHANGELOG.md or missing version details.{Font.END}')
    quit()
del date

# Verify that the CHANGELOG lines start with a hyphen and end with a period and a double space.
lines = [line for line in open('CHANGELOG.md').readlines() if not line.startswith('#') and not line.endswith('.  \n') and not line == '\n']
if len(lines) == 0:
    print(f'{Font.OK_GREEN}All lines in CHANGELOG.md seem correct.{Font.END}')
else:
    print(f'{Font.FAIL}{len(lines)} {"line" if len(lines) < 2 else "lines"} should start with a hyphen and end with a period and a double space: {lines}.{Font.END}')
    quit()

# Print warning every import between modules should be relative import
print(f'{Font.WARNING}All imports between modules should be relative imports.{Font.END}')
print(f'{Font.OK_GREEN}\n>>> Setup check passed successfuly. <<<{Font.END}')
