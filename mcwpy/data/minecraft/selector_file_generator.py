# -*- coding: ascii -*-
prefered_minecraft_version = '1.17.1'

if __name__ == '__main__':
    from mcwpy import Font
    import os

    print(f"{Font.WARN}Generating entities for Minecraft version {prefered_minecraft_version}!{Font.END}")

    with open(os.path.join(os.getcwd(), 'mcwpy', 'data', 'minecraft', 'selector.py'), 'w+') as f:
        # Imports
        f.write('# -*- coding: ascii\nfrom dataclasses import dataclass\n\n\n')

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

        # Subclasses
        for entity in (
            'player',
            'area_effect_cloud', 'armor_stand', 'arrow', 'axolotl',
            'bat', 'bee', 'blaze', 'boat',
            'cat', 'cave_spider', 'chest_minecart', 'chicken', 'cod', 'command_block_minecart', 'cow', 'creeper', 'dolphin', 'donkey', 'dragon_fireball', 'drowned',
            'egg', 'elder_guardian', 'end_crystal', 'ender_dragon', 'ender_pearl', 'enderman', 'endermite', 'evoker', 'evoker_fangs', 'experience_bottle', 'experience_orb', 'eye_of_ender',
            'falling_block', 'fireball', 'firework_rocket', 'fox', 'furnance_minecart', 
            'ghast', 'giant', 'glow_item_frame', 'glow_squid', 'goat', 'guardian',
            'hoglin', 'hopper_minecart', 'horse', 'husk', 
            'illusioner', 'iron_golem', 'item', 'item_frame',
            'lead', 'lightning_bolt', 'llama', 'llama_spit',
            'magma_cube', 'marker', 'minecart', 'mooshroom', 'mule',
            'ocelot',
            'painting', 'panda', 'parrot', 'phantom', 'pig', 'piglin', 'piglin_brute', 'pillager', 'polar_bear', 'potion', 'pufferfish',
            'rabbit', 'ravager',
            'salmon', 'sheep', 'shulker', 'shulker_bullet', 'silverfish', 'skeleton', 'skeleton_horse', 'slime', 'small_fireball', 'snow_golem', 'spawner_minecart', 'spectral_arrow', 'spider', 'squid', 'stray', 'strider',
            'tnt', 'tnt_minecart', 'trader_llama', 'trident', 'tropical_fish', 'turtle', 
            'vex', 'villager', 'vindicator',
            'wandering_trader', 'witch', 'wither_boss', 'wither_skeleton', 'wither_skull', 'wolf',
            'zoglin', 'zombie', 'zombie_horse', 'zombie_villager', 'zombified_piglin'

        ):
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
        ]) + '\n\n')

        # Functions
        f.write('\n\t'.join([
            '\t@classmethod',
            'def change(_, string: str, **kwargs) -> str:',
            '\tfor key_word in kwargs:',
            '\t\tif key_word in string[2:-1]:',
            '\t\t\t_start = string.index(key_word) + len(key_word) + 1',
            "\t\t\t_end = next((index for index, character in enumerate(string[_start:]) if character in {'}', ',', ']'}), len(string) - 1) + _start",
            '\t\t\tstring = string[:_start] + str(kwargs[key_word]) + string[_end:]',
            '\t\telse:',
            "\t\t\tstring = string + f'[{key_word}={kwargs[key_word]}]' if string[3] == '[' else string[:string.index(']')] + f',{key_word}={kwargs[key_word]}' + ']'",
            '\n\t\treturn string'
        ]) + '\n')
