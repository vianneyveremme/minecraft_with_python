# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                                 #
#       Code by Silvathor (in collaboration with Awhikax and Kikipunk)            #
#                                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

scoreboard objectives add silvathor_RANDOM dummy
scoreboard players set modulo silvathor_RANDOM 0
summon area_effect_cloud ~ ~ ~ {Tags:["silvathor_random_aec"],Age:1}
execute store result score @s silvathor_RANDOM run data get entity @e[type=area_effect_cloud,tag=silvathor_random_aec,limit=1] UUID[0]
scoreboard players operation @s silvathor_RANDOM %= modulo silvathor_RANDOM