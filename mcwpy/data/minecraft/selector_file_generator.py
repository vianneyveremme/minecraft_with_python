# -*- coding: ascii -*-
from entities import Entity


prefered_minecraft_version = '1.17.1'

if __name__ == '__main__':
    from mcwpy import Font
    import os

    print(f"{Font.WARN}Generating entities for Minecraft version {prefered_minecraft_version}!{Font.END}")

    with open(os.path.join(os.getcwd(), 'mcwpy', 'data', 'minecraft', 'selector.py'), 'w+') as f:
        # Imports
        f.write('# -*- coding: ascii -*-\nfrom dataclasses import dataclass\n\n\n')

        # Main class
        f.write('\n\t'.join([
            '@dataclass\nclass Selector:',
            "all = '@a'",
            "entities = '@e'",
            "furthest = '@e[sort=furthest]'",
            "nearest = '@e[sort=nearest]'",
            "random = '@e[sort=random]'",
            "self = '@s'"
        ]) + '\n\n')

        # Functions
        f.write('\n\t'.join([
            '\t@classmethod',
            'def set(_, string: str, **kwargs) -> str:',
            '\tfor key_word in kwargs:',
            '\t\tif key_word in string[2:-1]:',
            '\t\t\t_start = string.index(key_word) + len(key_word) + 1',
            "\t\t\t_end = next((index for index, character in enumerate(string[_start:]) if character in {'}', ',', ']'}), len(string) - 1) + _start",
            '\t\t\tstring = string[:_start] + str(kwargs[key_word]) + string[_end:]',
            '\t\telse:',
            "\t\t\tstring = string + f'[{key_word}={kwargs[key_word]}]' if string[3] == '[' else string[:string.index(']')] + f',{key_word}={kwargs[key_word]}' + ']'",
            '\n\t\treturn string'
        ]) + '\n\n')

        # Subclasses
        for entity in dir(Entity):
            if not entity.startswith('__'):
                f.write('\n\t\t'.join([
                    f"\t@dataclass\n\tclass {'_'.join(word.capitalize() for word in entity.split('_'))}:",
                    'all = ' + "'@" + ('a' if entity == 'player' else f'e[type=minecraft:{entity}]') + "'",
                    'furthest = ' + "'@" + (f'a[limit=1,sort=furthest]' if entity == 'player' else f'e[limit=1,sort=furthest,type=minecraft:{entity}]') + "'",
                    "nearest = " + "'@" + ('p' if entity == 'player' else f'e[limit=1,sort=nearest,type=minecraft:{entity}]') + "'",
                    "random = " + "'@" + ('r' if entity == 'player' else f'e[limit=1,sort=random,type=minecraft:{entity}]') + "'",
                ]) + '\n\n')
        
        # Custom classes
        f.write('\n\t\t'.join([
            '\t@dataclass\n\tclass Custom:',
            '# Short',
            "aec = '@e[type=minecraft:area_effect_cloud]'",
            "jean = '@e[type=minecraft:ender_dragon]'",
            "pillager_beast = '@e[type=minecraft:ravager]'",
            '# Named Binary Tag',
            "on_ground = '@e[nbt={OnGround:1b}]'"
        ]) + '\n')
