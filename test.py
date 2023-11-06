import turtle
from main import SolarSystem, Sun, Planet


solar_system = SolarSystem(width=1400, height=900)

sun = Sun(solar_system, mass=1e4, velocity=(0.03, 0.03))
planet = Planet(solar_system, mass=1e3, velocity=(
    0.04, -0.02), position=(0.02, 0.04))
sun.draw()
planet.draw()
while True:
    solar_system.update_all()

turtle.done()
