# [Minecraft](https://www.minecraft.net/download)-[Datapacks](https://minecraft.gamepedia.com/Data_Pack)-Generator  

## Installation:  
* First of all make sure you have one of the latest [Python](https://www.python.org/downloads/) version installed on your computer.  
* Ensure you also have [pip](https://pip.pypa.io/en/stable/installation/) installed: try running the command "`pip3 -V`" in a terminal.  
* If this gets you an error message follow [these steps](https://pip.pypa.io/en/stable/installation/) to install it.  
* Once you have [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) installed, run the command: "`pip3 install mcwpy`".  


## Usage:  
Now you should be able to import the library in your new [Python](https://www.python.org/downloads/) programs you can use the project below to help you get started with the library:  
```py 
from mcwpy import *
```  
* Create and compile your own datapack.  
* Once the datapack is generated, paste it in the *datapacks* folder of your [Minecraft](https://www.minecraft.net/download) world.  
* Type `/reload` to load the datapack.  
* Have fun playing with your brand new handmade datapack!  


## Example:  
```python
from mcwpy import *


# Since this is still in development, this should only print "test".
my_datapack = Datapack("My Datapack")
print('This example still needs to be created')
```  
