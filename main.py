from ursina import *

app = Ursina()
random_color = lambda: color.colors[random.choice(color.color_names)]

################################################################################

first_cube = Entity(model='cube', texture='white_cube', color=random_color(), rotation=(45, 25, 0))

def update():
	first_cube.rotation_x += 35 * time.dt
	first_cube.rotation_y += 20 * time.dt

################################################################################

app.run()
