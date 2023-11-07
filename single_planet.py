import turtle
from main import SolarSystem, Sun, Planet
import time

solar_system = SolarSystem(width=1400, height=900)

sun = Sun(solar_system, mass=1e4)
planet = Planet(solar_system, mass=1e3, velocity=[
    -0.4, -0.4], position=[5, 5])
sun.draw()
planet.draw()
while True:
    solar_system.update_all()
    solar_system.total_acc(planet)
    print(planet.velocity)
    time.sleep(1)


turtle.done()
