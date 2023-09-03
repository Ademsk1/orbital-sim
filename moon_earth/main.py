import numpy as np
import matplotlib.pyplot as plt
G = 6.67e-11 #Gravitational constant
M_e = 5.972e24
def distance_and_direction(r1, r2):
  vector_distance =  r2-r1
  distance = np.sqrt(vector_distance[0]**2 + vector_distance[1]**2)
  if distance==0:
    return np.array([0,0])
  unit_vector = vector_distance / distance
  return distance, unit_vector
def gravitational_field(m, r1, r2):
  #returns vectorised gravitational field
  d, r = distance_and_direction(r1,r2)
  gravitational_field_strength = -(G * m)/(d**2)
  return gravitational_field_strength * r 
  pass



# This is NOT the midpoint rule, but could be considered the "left-point rule"
# It doesnt seem feasible to use midpoint, we'd need a clearly defined value to integrate
def left_point_rule(v, r1, r2, m,dt):
  gravitational_acceleration_vector = gravitational_field(m,r1,r2)
  dv = gravitational_acceleration_vector * dt
  v +=dv
  r2 = r2 + v*dt
  return r2, v

"""
Midpoint rule
For points on t, [1,2,3,4,5] we are given the position [x,y] and velocity [vx, vy] at t[0].
We calculate the gravitational strength, f(x,y). 
velocity = integral (a * dt)
  |
  |
  |---*
a |///|
  |///|
  |///|  
  |---|---|---|---|---|---|
    0   1   2   3   4   5
             t

Given a velocity, the position of the particle moves over this time
  |
  |
  |
v |
  *---*
  |///|  
  |---|---|---|---|---|---|
  0   1   2   3   4   5
             t
And the position changed is the integral of velocity over time.

With a new position we recalculate the gravitational strength, integrate to get velocity, 
integrate to get position, and repeat the cycle. 

  |
  |
  *---*
a |///|---*       *---*
  |///|///|---*---|///|
  |///|///|///|///|///| 
  |---|---|---|---|---|---|
  0   1   2   3   4   5
             t

We currently do a left-point rule, which takes all the numbers and treats them as the left point of the 
rectangle over which we get the area. 
"""

"""
Simpsons rule

With Simpsons rule, we need to have 3 values, in order to integrate. f(t0), f(t1), f(t2). Once we have
the first of these, it should be straightforward to get f(t3), as we get the integration, find v,
then get the position through a similar integral, and then find f(t3). Then we can do Simpsons rule
with f(t3) 
"""


def generate_moons_journey(dt, num_of_orbits):
  starting_position_moon_perigree = ([0,360e6])
  earth_position_static = np.array([0,0])
  max_moon_velocity = np.array([1.082e3, 0])
  moon_period = np.int64(60*60*24*27.3)
  duration = moon_period * num_of_orbits
  if (dt > duration / 1000):
    raise Exception('For meaningful data, your \u0394t must be smaller than 1/1000th of the orbits duration.')
  moons_journey = np.zeros((np.int64(duration // dt)+1, 2))
  moon_vel = max_moon_velocity
  moons_journey[0] = starting_position_moon_perigree
  moon_position = moons_journey[0]
  for i in range(len(moons_journey)-1):
    moon_position, moon_vel = left_point_rule( moon_vel, earth_position_static,moon_position,M_e,dt)
    moons_journey[i+1] = moon_position
  return moons_journey



def plot_moons_path(moons_journey, dt):
  plt.scatter(moons_journey[::100,0], moons_journey[::100,1])
  plt.xlabel('X (m)')
  plt.ylabel('Y (m)')
  plt.gca().set_aspect('equal')
  plt.legend(f'dt = {dt}s')
  plt.show()
  plt.savefig('moons_path.png')


def main(dt):
  moons_journey = generate_moons_journey(dt, 2)
  np.savetxt(f'moons_journey_dt_{dt}s.txt', moons_journey)
  plot_moons_path(moons_journey, dt)


