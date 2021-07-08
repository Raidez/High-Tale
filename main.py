import random
from ursina import *

app = Ursina()
random_color = lambda: color.colors[random.choice(color.color_names)]

################################################################################

a_lot_of_cubes = list()
for x in range(16 * 16):
    random_position = (
        random.randint(-10, 10),
        random.randint(-10, 10),
        random.randint(-10, 10),
    )

    a_lot_of_cubes.append(
        Entity(
            model="cube",
            texture="white_cube",
            color=random_color(),
            position=random_position,
        )
    )

################################################################################

app.run()
