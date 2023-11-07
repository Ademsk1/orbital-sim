import turtle
from main import SolarSystem, Sun, Planet
import time

solar_system = SolarSystem(width=1400, height=900)

sun = Sun(solar_system, mass=1e4)
planet = Planet(solar_system, mass=1e3, velocity=[
    15, 0], position=[0, 50])

big_planet = Planet(solar_system, mass=5e3,
                    velocity=[-20, -4], position=[-25, 25])
big_planet = Planet(solar_system, mass=1e3,
                    velocity=[0, -1], position=[-69, -69])
big_planet = Planet(solar_system, mass=3e3,
                    velocity=[-5, -4], position=[-69, 2])
big_planet = Planet(solar_system, mass=2e4,
                    velocity=[0, 0], position=[-40, 40])
sun.draw()
planet.draw()
while True:
    solar_system.update_all()
    solar_system.total_acc(planet)
    solar_system.total_acc(sun)
    solar_system.total_acc(big_planet)
    print(planet.velocity)


turtle.done()
