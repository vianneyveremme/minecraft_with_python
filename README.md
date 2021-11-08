# [Minecraft](https://www.minecraft.net)-[Datapacks](https://minecraft.gamepedia.com/Data_Pack)-Generator  
[![Total alerts](https://img.shields.io/lgtm/alerts/g/vianneyveremme/minecraft_with_python.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/vianneyveremme/minecraft_with_python/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/vianneyveremme/minecraft_with_python.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/vianneyveremme/minecraft_with_python/context:python)

## Description:  
A new way of coding [Minecraft](https://www.minecraft.net).
[Minecraft](https://www.minecraft.net) is a game that you can play on your computer. It is a popular game for people who are interested in building their own worlds. And since a way to code the game itself has been implemented, I tried it. But it was not simple. So I decided to make a generator for the [Minecraft](https://www.minecraft.net) [Datapacks](https://minecraft.gamepedia.com/Data_Pack), so people can make their own [Datapacks](https://minecraft.gamepedia.com/Data_Pack) easily, even though they still need to know Python until I can make it look like [Scratch](https:/scratch.mit.edu) or something this easy.

## Installation:  
* First of all make sure you have one of the latest [Python](https://www.python.org/downloads/) version installed on your computer.  
* Ensure you also have [pip](https://pip.pypa.io/en/stable/installation/) installed: try running the command "`pip3 -V`" in a terminal.  
* If this gets you an error message follow [these steps](https://pip.pypa.io/en/stable/installation/) to install it.  
* Once you have [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) installed, run the command: "`pip3 install mcwpy`".  


## Usage:  
Now you should be able to import the library in your new [Python](https://www.python.org/downloads/) programs you can use the project below to help you get started with the library:  
```py 
import mcwpy
```  
* Create and compile your own datapack.  
* Once the datapack is generated, paste it in the *datapacks* folder of your [Minecraft](https://www.minecraft.net/download) world.  
* Type `/reload` to load the datapack.  
* Have fun playing with your brand new handmade datapack!  

### Example:  
```python
# -*- coding: ascii -*-
from mcwpy import *

workspace1 = Workspace(
    name = 'my_workspace',
    functions = {
        'load': 'tellraw @a {"text":"Datapack loaded!"}',
        'hello_world': 'say Hello World!'
    }
)

my_datapack = Datapack(
    title = 'My Datapack',
    pack_mcmeta = Pack_Meta(
        author = 'Myself',
        description = 'My very own Minecraft datapack',
        minecraft_version = Minecraft_Pack_Version.LATEST
    ),
    workspaces = [workspace1]
)

workspace2 = Workspace(
    functions = {
        'main': 'title @a actionbar {"text":"Hey!"}',
        'test': [
            'say Test',
            'execute as @s at @s run summon pig ~ ~ ~'
        ]
    }
)

my_datapack.append(workspace2)
my_datapack.compile()
```
```mcfunction
function my_workspace:hello_world
```
![Screenshot 2021-10-07 162422](https://user-images.githubusercontent.com/88092549/136458850-c71a3e5b-4351-498f-9161-9f2438f8ea91.png)

## Contributing:
If you want to contribute to this project, you can do so by forking it and sending a pull request, I am opened to any idea and contribution.

## Credits:
Thanks to [@theskyblockman](https://github.com/theskyblockman) for the idea of using workspaces.
Thanks to [@Silvathor](https://github.com/SilvaUnCompte) for the idea of redesigning the workspaces.
