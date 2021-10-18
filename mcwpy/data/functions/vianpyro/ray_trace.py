def ray_trace(function_name: str, score:str='vianpyro_RAY', condition: str | list=None, range: int=50, step: int | float=1, particles: str | list='flame'):
    if isinstance(particles, str):
        _particle_1 = f'particle {particles} ~ ~ ~ 0 0 0 0 1 force' if len(particles.split(' ')) == 1 else particles
        _particle_2 = f'particle minecraft:explosion ~ ~ ~ 0.5 0.5 0.5 0.01 10 force'
    elif  isinstance(particles, list):
        _particle_1 = f'particle {particles[0]} ~ ~ ~ 0 0 0 0 1 force' if len(particles[0].split(' ')) == 1 else particles[0]
        _particle_2 = f'particle {particles[1]} ~ ~ ~ 0 0 0 0 1 force' if len(particles[1].split(' ')) == 1 else particles[1]
    else:
        _particle_1 = f'particle minecraft:flame ~ ~ ~ 0 0 0 0 1 force'
        _particle_2 = f'particle minecraft:explosion ~ ~ ~ 0.5 0.5 0.5 0.01 10 force'


    return '\n'.join([
        f'scoreboard objectives add {score} dummy',
        '# No condition' if condition is None else (
            condition if isinstance(condition, str) else '\n'.join(condition)
        ),
        _particle_1,
        f'scoreboard players add @s {score} 1',
        f'execute unless block ~ ~ ~ air run particle {_particle_2}',
        f'execute unless score @s {score} matches {range}.. if block ~ ~ ~ air positioned ^ ^ ^{step} run function {function_name}',
        f'scoreboard players reset @s {score}'
    ])

print(ray_trace('vianpyro:ray_trace'))