import turtle
import math
import itertools


class SolarSystemBody(turtle.Turtle):
    min_display_size = 20
    display_log_base = 1.1

    def __init__(self, solar_system, mass, position=[0, 0], velocity=[0, 0]):
        super().__init__()
        self.mass = mass
        self.setposition(position)
        self.velocity = velocity
        self.penup()
        self.hideturtle()
        solar_system.add_body(self)
        self.display_size = max(math.log(self.mass), self.display_log_base)

    def draw(self):
        self.clear()
        self.dot(self.display_size)

    def move(self):
        self.setx(self.xcor() + self.velocity[0]*0.02)
        self.sety(self.ycor() + self.velocity[1]*0.02)


class SolarSystem:
    def __init__(self, width, height):
        self.solar_system = turtle.Screen()
        self.solar_system.tracer(0)  # what does this do?
        self.solar_system.setup(width, height)
        self.solar_system.bgcolor('black')
        self.bodies = []

    def add_body(self, body):
        self.bodies.append(body)

    def remove_body(self, body):
        self.bodies.remove(body)

    def get_acceleration(self, body1, body2):
        p1x, p1y = body1.xcor(), body1.ycor()
        p2x, p2y = body2.xcor(), body2.ycor()
        distanceX = (p2x-p1x)
        distanceY = (p2y - p1y)
        if (distanceX**2 + distanceY**2 == 0):
            return
        absoluteDistance = (distanceX**2 + distanceY**2)**(0.5)

        a = body2.mass / (distanceX**2 + distanceY**2)
        ax = a * (distanceX)/absoluteDistance
        print(f'ax {ax}')
        ay = a * (distanceY)/absoluteDistance
        return [ax, ay]

    def total_acc(self, chosen_body):
        acc = [0, 0]
        for body in self.bodies:
            if (body != chosen_body):
                new_acc = self.get_acceleration(chosen_body, body)
                acc[0] += new_acc[0]*0.02
                acc[1] += new_acc[1]*0.02
        chosen_body.velocity[0] += acc[0]
        chosen_body.velocity[1] += acc[1]

    def update_all(self):
        for body in self.bodies:
            body.move()
            body.draw()
        self.solar_system.update()

    pass


class Sun(SolarSystemBody):
    def __init__(self, solar_system, mass, position=[0, 0], velocity=[0, 0]):
        super().__init__(solar_system, mass, position, velocity)
        self.color('yellow')
    pass


class Planet(SolarSystemBody):
    colours = itertools.cycle(['red', 'green', 'yellow'])

    def __init__(self, solar_system, mass, position, velocity):
        super().__init__(solar_system, mass, position, velocity)
        self.color(next(Planet.colours))
