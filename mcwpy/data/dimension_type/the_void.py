# -*- coding: ascii -*-
from ... import utility

def the_void(minecraft_pack_format: str=None) -> dict:
    match minecraft_pack_format:
        case utility.Minecraft_Pack_Version.v1_18_2:
            return {
                "ultrawarm": False, "natural": False, "piglin_safe": False,
                "respawn_anchor_works": False, "bed_works": False,
                "has_raids": False, "has_skylight": True, "has_ceiling": False,
                "coordinate_scale": 1, "ambient_light": 0,
                "logical_height": 384, "min_y": -64, "height": 384,
                "infiniburn": "#minecraft:infiniburn_overworld"
            }
        case _:
            raise ValueError(f'{utility.Font.ERROR}This minecraft pack format: {minecraft_pack_format} is not supported at the moment!{utility.Font.END}')
