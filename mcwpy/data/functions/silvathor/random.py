def random(maximum: int=0, score: str='silvathor_RANDOM'):
    """
    Return a random integer in range [0, maximum[.

    :param maximum: The maximum value of the random number (excluded).
    :param score: The name of the Minecraft score for the random number.
    :return: A random number.
    """
    score.lower().replace(' ', '_')
    
    return '\n'.join([
        f'scoreboard objectives add {score} dummy',
        f'scoreboard players set maximum {score} {maximum}',
        f'summon area_effect_cloud ~ ~ ~ {{Tags:["{score}_aec"],Age:1}}',
        f'execute store result score @s {score} run data get entity @e[type=area_effect_cloud,tag={score}_aec,limit=1] UUID[0]',
        f'scoreboard players operation @s {score} %= maximum {score}',
    ])
