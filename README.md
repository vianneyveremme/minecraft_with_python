# [Minecraft](https://www.minecraft.net)-[Datapacks](https://minecraft.gamepedia.com/Data_Pack)-Generator  

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
import mcwpy

datapack = mcwpy.Datapack(
    pack_mcmeta=mcwpy.Pack_Meta(
        author="<Your name here>",
        description="<Description of your pack here>",
        minecraft_version=mcwpy.Minecraft_Pack_Version.LATEST
    ),
    workspaces=[
        mcwpy.Workspace(
            content={'function': {
                'test': 'say Hello World!',
                'load': 'tellraw @a {"text":"Datapack successfuly loaded!","color":"green"}',
                "main": 'effect give @a speed 1 1 true'
            }},
            workspaces=[
                mcwpy.Workspace(content={'load': 'say Hello World 2!'}),
                mcwpy.Workspace(content={'test2': 'say Hello World!'}),
            ]
        ),
        mcwpy.Workspace(
            name='workspace_2',
            content={'function': {
                'load': 'say Hello World 2!'
            }}
        )
    ],
    replace_existing=True,
    auto_compile=True
)
```  

## Contributing:
If you want to contribute to this project, you can do so by forking it and sending a pull request, I am opened to any idea and contribution.

## Credits:
Thanks to [@theskyblockman](https://github.com/theskyblockman) for the idea of using workspaces.
