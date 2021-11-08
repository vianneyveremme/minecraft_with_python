# -*- coding: ascii -*-
from dataclasses import dataclass


@dataclass
class Selector:
	all = '@a'
	entities = '@e'
	furthest = '@e[sort=furthest]'
	nearest = '@e[sort=nearest]'
	random = '@e[sort=random]'
	self = '@s'

	@dataclass
	class Player:
		all = '@a'
		furthest = '@a[limit=1,sort=furthest]'
		nearest = '@p'
		random = '@r'

	@dataclass
	class Area_Effect_Cloud:
		all = '@e[type=minecraft:area_effect_cloud]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:area_effect_cloud]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:area_effect_cloud]'
		random = '@e[limit=1,sort=random,type=minecraft:area_effect_cloud]'

	@dataclass
	class Armor_Stand:
		all = '@e[type=minecraft:armor_stand]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:armor_stand]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:armor_stand]'
		random = '@e[limit=1,sort=random,type=minecraft:armor_stand]'

	@dataclass
	class Arrow:
		all = '@e[type=minecraft:arrow]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:arrow]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:arrow]'
		random = '@e[limit=1,sort=random,type=minecraft:arrow]'

	@dataclass
	class Axolotl:
		all = '@e[type=minecraft:axolotl]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:axolotl]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:axolotl]'
		random = '@e[limit=1,sort=random,type=minecraft:axolotl]'

	@dataclass
	class Bat:
		all = '@e[type=minecraft:bat]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:bat]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:bat]'
		random = '@e[limit=1,sort=random,type=minecraft:bat]'

	@dataclass
	class Bee:
		all = '@e[type=minecraft:bee]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:bee]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:bee]'
		random = '@e[limit=1,sort=random,type=minecraft:bee]'

	@dataclass
	class Blaze:
		all = '@e[type=minecraft:blaze]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:blaze]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:blaze]'
		random = '@e[limit=1,sort=random,type=minecraft:blaze]'

	@dataclass
	class Boat:
		all = '@e[type=minecraft:boat]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:boat]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:boat]'
		random = '@e[limit=1,sort=random,type=minecraft:boat]'

	@dataclass
	class Cat:
		all = '@e[type=minecraft:cat]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:cat]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:cat]'
		random = '@e[limit=1,sort=random,type=minecraft:cat]'

	@dataclass
	class Cave_Spider:
		all = '@e[type=minecraft:cave_spider]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:cave_spider]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:cave_spider]'
		random = '@e[limit=1,sort=random,type=minecraft:cave_spider]'

	@dataclass
	class Chest_Minecart:
		all = '@e[type=minecraft:chest_minecart]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:chest_minecart]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:chest_minecart]'
		random = '@e[limit=1,sort=random,type=minecraft:chest_minecart]'

	@dataclass
	class Chicken:
		all = '@e[type=minecraft:chicken]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:chicken]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:chicken]'
		random = '@e[limit=1,sort=random,type=minecraft:chicken]'

	@dataclass
	class Cod:
		all = '@e[type=minecraft:cod]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:cod]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:cod]'
		random = '@e[limit=1,sort=random,type=minecraft:cod]'

	@dataclass
	class Command_Block_Minecart:
		all = '@e[type=minecraft:command_block_minecart]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:command_block_minecart]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:command_block_minecart]'
		random = '@e[limit=1,sort=random,type=minecraft:command_block_minecart]'

	@dataclass
	class Cow:
		all = '@e[type=minecraft:cow]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:cow]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:cow]'
		random = '@e[limit=1,sort=random,type=minecraft:cow]'

	@dataclass
	class Creeper:
		all = '@e[type=minecraft:creeper]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:creeper]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:creeper]'
		random = '@e[limit=1,sort=random,type=minecraft:creeper]'

	@dataclass
	class Dolphin:
		all = '@e[type=minecraft:dolphin]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:dolphin]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:dolphin]'
		random = '@e[limit=1,sort=random,type=minecraft:dolphin]'

	@dataclass
	class Donkey:
		all = '@e[type=minecraft:donkey]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:donkey]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:donkey]'
		random = '@e[limit=1,sort=random,type=minecraft:donkey]'

	@dataclass
	class Dragon_Fireball:
		all = '@e[type=minecraft:dragon_fireball]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:dragon_fireball]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:dragon_fireball]'
		random = '@e[limit=1,sort=random,type=minecraft:dragon_fireball]'

	@dataclass
	class Drowned:
		all = '@e[type=minecraft:drowned]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:drowned]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:drowned]'
		random = '@e[limit=1,sort=random,type=minecraft:drowned]'

	@dataclass
	class Egg:
		all = '@e[type=minecraft:egg]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:egg]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:egg]'
		random = '@e[limit=1,sort=random,type=minecraft:egg]'

	@dataclass
	class Elder_Guardian:
		all = '@e[type=minecraft:elder_guardian]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:elder_guardian]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:elder_guardian]'
		random = '@e[limit=1,sort=random,type=minecraft:elder_guardian]'

	@dataclass
	class End_Crystal:
		all = '@e[type=minecraft:end_crystal]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:end_crystal]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:end_crystal]'
		random = '@e[limit=1,sort=random,type=minecraft:end_crystal]'

	@dataclass
	class Ender_Dragon:
		all = '@e[type=minecraft:ender_dragon]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:ender_dragon]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:ender_dragon]'
		random = '@e[limit=1,sort=random,type=minecraft:ender_dragon]'

	@dataclass
	class Ender_Pearl:
		all = '@e[type=minecraft:ender_pearl]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:ender_pearl]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:ender_pearl]'
		random = '@e[limit=1,sort=random,type=minecraft:ender_pearl]'

	@dataclass
	class Enderman:
		all = '@e[type=minecraft:enderman]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:enderman]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:enderman]'
		random = '@e[limit=1,sort=random,type=minecraft:enderman]'

	@dataclass
	class Endermite:
		all = '@e[type=minecraft:endermite]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:endermite]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:endermite]'
		random = '@e[limit=1,sort=random,type=minecraft:endermite]'

	@dataclass
	class Evoker:
		all = '@e[type=minecraft:evoker]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:evoker]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:evoker]'
		random = '@e[limit=1,sort=random,type=minecraft:evoker]'

	@dataclass
	class Evoker_Fangs:
		all = '@e[type=minecraft:evoker_fangs]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:evoker_fangs]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:evoker_fangs]'
		random = '@e[limit=1,sort=random,type=minecraft:evoker_fangs]'

	@dataclass
	class Experience_Bottle:
		all = '@e[type=minecraft:experience_bottle]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:experience_bottle]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:experience_bottle]'
		random = '@e[limit=1,sort=random,type=minecraft:experience_bottle]'

	@dataclass
	class Experience_Orb:
		all = '@e[type=minecraft:experience_orb]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:experience_orb]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:experience_orb]'
		random = '@e[limit=1,sort=random,type=minecraft:experience_orb]'

	@dataclass
	class Eye_Of_Ender:
		all = '@e[type=minecraft:eye_of_ender]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:eye_of_ender]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:eye_of_ender]'
		random = '@e[limit=1,sort=random,type=minecraft:eye_of_ender]'

	@dataclass
	class Falling_Block:
		all = '@e[type=minecraft:falling_block]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:falling_block]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:falling_block]'
		random = '@e[limit=1,sort=random,type=minecraft:falling_block]'

	@dataclass
	class Fireball:
		all = '@e[type=minecraft:fireball]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:fireball]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:fireball]'
		random = '@e[limit=1,sort=random,type=minecraft:fireball]'

	@dataclass
	class Firework_Rocket:
		all = '@e[type=minecraft:firework_rocket]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:firework_rocket]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:firework_rocket]'
		random = '@e[limit=1,sort=random,type=minecraft:firework_rocket]'

	@dataclass
	class Fox:
		all = '@e[type=minecraft:fox]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:fox]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:fox]'
		random = '@e[limit=1,sort=random,type=minecraft:fox]'

	@dataclass
	class Furnance_Minecart:
		all = '@e[type=minecraft:furnance_minecart]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:furnance_minecart]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:furnance_minecart]'
		random = '@e[limit=1,sort=random,type=minecraft:furnance_minecart]'

	@dataclass
	class Ghast:
		all = '@e[type=minecraft:ghast]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:ghast]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:ghast]'
		random = '@e[limit=1,sort=random,type=minecraft:ghast]'

	@dataclass
	class Giant:
		all = '@e[type=minecraft:giant]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:giant]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:giant]'
		random = '@e[limit=1,sort=random,type=minecraft:giant]'

	@dataclass
	class Glow_Item_Frame:
		all = '@e[type=minecraft:glow_item_frame]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:glow_item_frame]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:glow_item_frame]'
		random = '@e[limit=1,sort=random,type=minecraft:glow_item_frame]'

	@dataclass
	class Glow_Squid:
		all = '@e[type=minecraft:glow_squid]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:glow_squid]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:glow_squid]'
		random = '@e[limit=1,sort=random,type=minecraft:glow_squid]'

	@dataclass
	class Goat:
		all = '@e[type=minecraft:goat]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:goat]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:goat]'
		random = '@e[limit=1,sort=random,type=minecraft:goat]'

	@dataclass
	class Guardian:
		all = '@e[type=minecraft:guardian]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:guardian]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:guardian]'
		random = '@e[limit=1,sort=random,type=minecraft:guardian]'

	@dataclass
	class Hoglin:
		all = '@e[type=minecraft:hoglin]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:hoglin]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:hoglin]'
		random = '@e[limit=1,sort=random,type=minecraft:hoglin]'

	@dataclass
	class Hopper_Minecart:
		all = '@e[type=minecraft:hopper_minecart]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:hopper_minecart]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:hopper_minecart]'
		random = '@e[limit=1,sort=random,type=minecraft:hopper_minecart]'

	@dataclass
	class Horse:
		all = '@e[type=minecraft:horse]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:horse]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:horse]'
		random = '@e[limit=1,sort=random,type=minecraft:horse]'

	@dataclass
	class Husk:
		all = '@e[type=minecraft:husk]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:husk]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:husk]'
		random = '@e[limit=1,sort=random,type=minecraft:husk]'

	@dataclass
	class Illusioner:
		all = '@e[type=minecraft:illusioner]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:illusioner]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:illusioner]'
		random = '@e[limit=1,sort=random,type=minecraft:illusioner]'

	@dataclass
	class Iron_Golem:
		all = '@e[type=minecraft:iron_golem]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:iron_golem]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:iron_golem]'
		random = '@e[limit=1,sort=random,type=minecraft:iron_golem]'

	@dataclass
	class Item:
		all = '@e[type=minecraft:item]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:item]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:item]'
		random = '@e[limit=1,sort=random,type=minecraft:item]'

	@dataclass
	class Item_Frame:
		all = '@e[type=minecraft:item_frame]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:item_frame]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:item_frame]'
		random = '@e[limit=1,sort=random,type=minecraft:item_frame]'

	@dataclass
	class Lead:
		all = '@e[type=minecraft:lead]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:lead]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:lead]'
		random = '@e[limit=1,sort=random,type=minecraft:lead]'

	@dataclass
	class Lightning_Bolt:
		all = '@e[type=minecraft:lightning_bolt]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:lightning_bolt]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:lightning_bolt]'
		random = '@e[limit=1,sort=random,type=minecraft:lightning_bolt]'

	@dataclass
	class Llama:
		all = '@e[type=minecraft:llama]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:llama]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:llama]'
		random = '@e[limit=1,sort=random,type=minecraft:llama]'

	@dataclass
	class Llama_Spit:
		all = '@e[type=minecraft:llama_spit]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:llama_spit]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:llama_spit]'
		random = '@e[limit=1,sort=random,type=minecraft:llama_spit]'

	@dataclass
	class Magma_Cube:
		all = '@e[type=minecraft:magma_cube]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:magma_cube]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:magma_cube]'
		random = '@e[limit=1,sort=random,type=minecraft:magma_cube]'

	@dataclass
	class Marker:
		all = '@e[type=minecraft:marker]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:marker]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:marker]'
		random = '@e[limit=1,sort=random,type=minecraft:marker]'

	@dataclass
	class Minecart:
		all = '@e[type=minecraft:minecart]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:minecart]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:minecart]'
		random = '@e[limit=1,sort=random,type=minecraft:minecart]'

	@dataclass
	class Mooshroom:
		all = '@e[type=minecraft:mooshroom]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:mooshroom]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:mooshroom]'
		random = '@e[limit=1,sort=random,type=minecraft:mooshroom]'

	@dataclass
	class Mule:
		all = '@e[type=minecraft:mule]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:mule]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:mule]'
		random = '@e[limit=1,sort=random,type=minecraft:mule]'

	@dataclass
	class Ocelot:
		all = '@e[type=minecraft:ocelot]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:ocelot]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:ocelot]'
		random = '@e[limit=1,sort=random,type=minecraft:ocelot]'

	@dataclass
	class Painting:
		all = '@e[type=minecraft:painting]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:painting]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:painting]'
		random = '@e[limit=1,sort=random,type=minecraft:painting]'

	@dataclass
	class Panda:
		all = '@e[type=minecraft:panda]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:panda]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:panda]'
		random = '@e[limit=1,sort=random,type=minecraft:panda]'

	@dataclass
	class Parrot:
		all = '@e[type=minecraft:parrot]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:parrot]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:parrot]'
		random = '@e[limit=1,sort=random,type=minecraft:parrot]'

	@dataclass
	class Phantom:
		all = '@e[type=minecraft:phantom]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:phantom]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:phantom]'
		random = '@e[limit=1,sort=random,type=minecraft:phantom]'

	@dataclass
	class Pig:
		all = '@e[type=minecraft:pig]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:pig]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:pig]'
		random = '@e[limit=1,sort=random,type=minecraft:pig]'

	@dataclass
	class Piglin:
		all = '@e[type=minecraft:piglin]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:piglin]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:piglin]'
		random = '@e[limit=1,sort=random,type=minecraft:piglin]'

	@dataclass
	class Piglin_Brute:
		all = '@e[type=minecraft:piglin_brute]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:piglin_brute]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:piglin_brute]'
		random = '@e[limit=1,sort=random,type=minecraft:piglin_brute]'

	@dataclass
	class Pillager:
		all = '@e[type=minecraft:pillager]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:pillager]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:pillager]'
		random = '@e[limit=1,sort=random,type=minecraft:pillager]'

	@dataclass
	class Polar_Bear:
		all = '@e[type=minecraft:polar_bear]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:polar_bear]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:polar_bear]'
		random = '@e[limit=1,sort=random,type=minecraft:polar_bear]'

	@dataclass
	class Potion:
		all = '@e[type=minecraft:potion]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:potion]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:potion]'
		random = '@e[limit=1,sort=random,type=minecraft:potion]'

	@dataclass
	class Pufferfish:
		all = '@e[type=minecraft:pufferfish]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:pufferfish]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:pufferfish]'
		random = '@e[limit=1,sort=random,type=minecraft:pufferfish]'

	@dataclass
	class Rabbit:
		all = '@e[type=minecraft:rabbit]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:rabbit]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:rabbit]'
		random = '@e[limit=1,sort=random,type=minecraft:rabbit]'

	@dataclass
	class Ravager:
		all = '@e[type=minecraft:ravager]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:ravager]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:ravager]'
		random = '@e[limit=1,sort=random,type=minecraft:ravager]'

	@dataclass
	class Salmon:
		all = '@e[type=minecraft:salmon]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:salmon]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:salmon]'
		random = '@e[limit=1,sort=random,type=minecraft:salmon]'

	@dataclass
	class Sheep:
		all = '@e[type=minecraft:sheep]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:sheep]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:sheep]'
		random = '@e[limit=1,sort=random,type=minecraft:sheep]'

	@dataclass
	class Shulker:
		all = '@e[type=minecraft:shulker]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:shulker]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:shulker]'
		random = '@e[limit=1,sort=random,type=minecraft:shulker]'

	@dataclass
	class Shulker_Bullet:
		all = '@e[type=minecraft:shulker_bullet]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:shulker_bullet]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:shulker_bullet]'
		random = '@e[limit=1,sort=random,type=minecraft:shulker_bullet]'

	@dataclass
	class Silverfish:
		all = '@e[type=minecraft:silverfish]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:silverfish]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:silverfish]'
		random = '@e[limit=1,sort=random,type=minecraft:silverfish]'

	@dataclass
	class Skeleton:
		all = '@e[type=minecraft:skeleton]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:skeleton]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:skeleton]'
		random = '@e[limit=1,sort=random,type=minecraft:skeleton]'

	@dataclass
	class Skeleton_Horse:
		all = '@e[type=minecraft:skeleton_horse]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:skeleton_horse]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:skeleton_horse]'
		random = '@e[limit=1,sort=random,type=minecraft:skeleton_horse]'

	@dataclass
	class Slime:
		all = '@e[type=minecraft:slime]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:slime]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:slime]'
		random = '@e[limit=1,sort=random,type=minecraft:slime]'

	@dataclass
	class Small_Fireball:
		all = '@e[type=minecraft:small_fireball]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:small_fireball]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:small_fireball]'
		random = '@e[limit=1,sort=random,type=minecraft:small_fireball]'

	@dataclass
	class Snow_Golem:
		all = '@e[type=minecraft:snow_golem]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:snow_golem]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:snow_golem]'
		random = '@e[limit=1,sort=random,type=minecraft:snow_golem]'

	@dataclass
	class Spawner_Minecart:
		all = '@e[type=minecraft:spawner_minecart]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:spawner_minecart]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:spawner_minecart]'
		random = '@e[limit=1,sort=random,type=minecraft:spawner_minecart]'

	@dataclass
	class Spectral_Arrow:
		all = '@e[type=minecraft:spectral_arrow]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:spectral_arrow]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:spectral_arrow]'
		random = '@e[limit=1,sort=random,type=minecraft:spectral_arrow]'

	@dataclass
	class Spider:
		all = '@e[type=minecraft:spider]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:spider]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:spider]'
		random = '@e[limit=1,sort=random,type=minecraft:spider]'

	@dataclass
	class Squid:
		all = '@e[type=minecraft:squid]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:squid]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:squid]'
		random = '@e[limit=1,sort=random,type=minecraft:squid]'

	@dataclass
	class Stray:
		all = '@e[type=minecraft:stray]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:stray]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:stray]'
		random = '@e[limit=1,sort=random,type=minecraft:stray]'

	@dataclass
	class Strider:
		all = '@e[type=minecraft:strider]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:strider]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:strider]'
		random = '@e[limit=1,sort=random,type=minecraft:strider]'

	@dataclass
	class Tnt:
		all = '@e[type=minecraft:tnt]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:tnt]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:tnt]'
		random = '@e[limit=1,sort=random,type=minecraft:tnt]'

	@dataclass
	class Tnt_Minecart:
		all = '@e[type=minecraft:tnt_minecart]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:tnt_minecart]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:tnt_minecart]'
		random = '@e[limit=1,sort=random,type=minecraft:tnt_minecart]'

	@dataclass
	class Trader_Llama:
		all = '@e[type=minecraft:trader_llama]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:trader_llama]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:trader_llama]'
		random = '@e[limit=1,sort=random,type=minecraft:trader_llama]'

	@dataclass
	class Trident:
		all = '@e[type=minecraft:trident]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:trident]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:trident]'
		random = '@e[limit=1,sort=random,type=minecraft:trident]'

	@dataclass
	class Tropical_Fish:
		all = '@e[type=minecraft:tropical_fish]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:tropical_fish]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:tropical_fish]'
		random = '@e[limit=1,sort=random,type=minecraft:tropical_fish]'

	@dataclass
	class Turtle:
		all = '@e[type=minecraft:turtle]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:turtle]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:turtle]'
		random = '@e[limit=1,sort=random,type=minecraft:turtle]'

	@dataclass
	class Vex:
		all = '@e[type=minecraft:vex]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:vex]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:vex]'
		random = '@e[limit=1,sort=random,type=minecraft:vex]'

	@dataclass
	class Villager:
		all = '@e[type=minecraft:villager]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:villager]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:villager]'
		random = '@e[limit=1,sort=random,type=minecraft:villager]'

	@dataclass
	class Vindicator:
		all = '@e[type=minecraft:vindicator]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:vindicator]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:vindicator]'
		random = '@e[limit=1,sort=random,type=minecraft:vindicator]'

	@dataclass
	class Wandering_Trader:
		all = '@e[type=minecraft:wandering_trader]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:wandering_trader]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:wandering_trader]'
		random = '@e[limit=1,sort=random,type=minecraft:wandering_trader]'

	@dataclass
	class Witch:
		all = '@e[type=minecraft:witch]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:witch]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:witch]'
		random = '@e[limit=1,sort=random,type=minecraft:witch]'

	@dataclass
	class Wither_Boss:
		all = '@e[type=minecraft:wither_boss]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:wither_boss]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:wither_boss]'
		random = '@e[limit=1,sort=random,type=minecraft:wither_boss]'

	@dataclass
	class Wither_Skeleton:
		all = '@e[type=minecraft:wither_skeleton]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:wither_skeleton]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:wither_skeleton]'
		random = '@e[limit=1,sort=random,type=minecraft:wither_skeleton]'

	@dataclass
	class Wither_Skull:
		all = '@e[type=minecraft:wither_skull]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:wither_skull]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:wither_skull]'
		random = '@e[limit=1,sort=random,type=minecraft:wither_skull]'

	@dataclass
	class Wolf:
		all = '@e[type=minecraft:wolf]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:wolf]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:wolf]'
		random = '@e[limit=1,sort=random,type=minecraft:wolf]'

	@dataclass
	class Zoglin:
		all = '@e[type=minecraft:zoglin]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:zoglin]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:zoglin]'
		random = '@e[limit=1,sort=random,type=minecraft:zoglin]'

	@dataclass
	class Zombie:
		all = '@e[type=minecraft:zombie]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:zombie]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:zombie]'
		random = '@e[limit=1,sort=random,type=minecraft:zombie]'

	@dataclass
	class Zombie_Horse:
		all = '@e[type=minecraft:zombie_horse]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:zombie_horse]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:zombie_horse]'
		random = '@e[limit=1,sort=random,type=minecraft:zombie_horse]'

	@dataclass
	class Zombie_Villager:
		all = '@e[type=minecraft:zombie_villager]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:zombie_villager]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:zombie_villager]'
		random = '@e[limit=1,sort=random,type=minecraft:zombie_villager]'

	@dataclass
	class Zombified_Piglin:
		all = '@e[type=minecraft:zombified_piglin]'
		furthest = '@e[limit=1,sort=furthest,type=minecraft:zombified_piglin]'
		nearest = '@e[limit=1,sort=nearest,type=minecraft:zombified_piglin]'
		random = '@e[limit=1,sort=random,type=minecraft:zombified_piglin]'

	@dataclass
	class Custom:
		# Short
		aec = '@e[type=minecraft:area_effect_cloud]'
		jean = '@e[type=minecraft:ender_dragon]'
		pillager_beast = '@e[type=minecraft:ravager]'
		# Named Binary Tag
		on_ground = '@e[nbt={OnGround:1b}]'

	@classmethod
	def change(_, string: str, **kwargs) -> str:
		for key_word in kwargs:
			if key_word in string[2:-1]:
				_start = string.index(key_word) + len(key_word) + 1
				_end = next((index for index, character in enumerate(string[_start:]) if character in {'}', ',', ']'}), len(string) - 1) + _start
				string = string[:_start] + str(kwargs[key_word]) + string[_end:]
			else:
				string = string + f'[{key_word}={kwargs[key_word]}]' if string[3] == '[' else string[:string.index(']')] + f',{key_word}={kwargs[key_word]}' + ']'
	
		return string
