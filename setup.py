# -*- coding: utf-8 -*-
"""
- Use 'python3 setup.py sdist' in a terminal to create the package.  
- Use 'twine upload --repository-url https://upload.pypi.org/legacy/ dist/*' to upload the package on pypi.  
"""
from setuptools import setup, find_packages
from _version import __version__

classifiers = [
    'Development Status :: 1 - Planning',
    'Intended Audience :: Customer Service',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: End Users/Desktop',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9'
    
]

setup(
    author='Vianpyro',
    author_email='vianney.veremme@gmail.com',
    classifiers=classifiers,
    description='A new way to create Minecraft datapacks',
    install_requires=open('REQUIREMENTS.txt').read(),
    keywords=['Minecraft', 'Datapack', 'Function', 'MCFunction'],
    license='MIT',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    long_description_content_type='text/markdown',
    name='mcwpy',
    packages=find_packages(exclude=['tests']),
    py_modules=['ansi_escape_sequences', 'datapack', 'datapack', 'test'],
    url='https://github.com/vianneyveremme/minecraft_with_python',
    version=__version__,
    zip_safe=False
)
