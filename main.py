import random
import numpy as np
from ursina import *

app = Ursina()
random_color = lambda: color.colors[random.choice(color.color_names)]

################################################################################

camera.position = (7.5, 15, -20)
camera.rotation = (30, 0, 0)

world = np.ones((16, 16), dtype=int)
for (x, z), value in np.ndenumerate(world):
    Entity(
        model="cube",
        collider="box",
        texture="white_cube",
        color=random_color(),
        position=(x, 0, z),
    )

################################################################################

app.run()
