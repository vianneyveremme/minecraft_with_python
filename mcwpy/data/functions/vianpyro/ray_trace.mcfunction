# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                                 #
#                                Code by Vianpyro                                 #
#                                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

scoreboard objectives add vianpyro_RAY dummy
scoreboard objectives add vianpyro_RAYCOND minecraft.used:minecraft.carrot_on_a_stick
scoreboard players reset @s[scores={vianpyro_RAYCOND=1..}] vianpyro_RAYCOND
particle minecraft:flame ~ ~ ~ 0 0 0 0 1 force
scoreboard players add @s vianpyro_RAY 1
execute unless block ~ ~ ~ air run particle minecraft:explosion ~ ~ ~ 0.5 0.5 0.5 0.01 10 force
execute unless score @s vianpyro_RAY matches 50.. if block ~ ~ ~ air positioned ^ ^ ^1 run function vianpyro:ray_trace
scoreboard players reset @s vianpyro_RAY
