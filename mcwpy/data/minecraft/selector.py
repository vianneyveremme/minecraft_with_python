# -*- coding: ascii -*-
from dataclasses import dataclass


@dataclass
class Selector:
    all = '@a'
    entity = '@e'
    furthest = '@e[sort=furthest]'
    nearest = '@p'
    random = '@r'
    self = '@s'

    @dataclass
    class Player:
        all = '@a'
        furthest = '@a[limit=1,sort=furthest]'
        nearest = '@p'
        random = '@r'
        self = '@s'

    @dataclass
    class Custom:
        # Short
        aec = '@e[type=minecraft:area_effect_cloud]'

        # Named Binary Tag
        on_ground = '@e[nbt={OnGround:1b}]'
