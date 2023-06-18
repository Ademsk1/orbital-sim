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


def simple_integration(v, r1, r2, m,dt):
  gravitational_acceleration_vector = gravitational_field(m,r1,r2)
  dv = gravitational_acceleration_vector * dt
  v +=dv
  r2 = r2 + v*dt
  return r2, v



def generate_moons_journey():
  starting_position_moon_perigree = ([0,360e6])
  earth_position_static = np.array([0,0])
  max_moon_velocity = np.array([1.082e3, 0])
  dt = 1 #1s
  moon_period = np.int64(60*60*24*27.3)
  moons_journey = np.zeros((np.int64(moon_period // dt)+1, 2))
  moon_vel = max_moon_velocity
  moons_journey[0] = starting_position_moon_perigree
  moon_position = moons_journey[0]
  for i in range(moon_period):
    moon_position, moon_vel = simple_integration( moon_vel, 
                                                  earth_position_static,
                                                  moon_position,
                                                  M_e,
                                                  dt)
    moons_journey[i+1] = moon_position
  return moons_journey


def plot_moons_path(moons_journey):
  plt.scatter(moons_journey[::100,0], moons_journey[::100,1])
  plt.xlabel('X (m)')
  plt.ylabel('Y (m)')
  #plt.gca().set_aspect('equal')
  plt.show()


def main():
  moons_journey = generate_moons_journey()
  plot_moons_path(moons_journey)

main()
