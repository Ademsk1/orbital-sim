import numpy as np
import matplotlib.pyplot as plt
G = 6.67e-11 #Gravitational constant

def distance_and_direction(r1, r2):
  vector_distance = (r1-r2)
  distance = np.sqrt(vector_distance[0]**2 + vector_distance[1]**2)
  unit_vector = vector_distance / distance
  return distance, unit_vector
def gravitational_field(m, r1, r2):
  #returns vectorised gravitational field
  d, r = distance_and_direction(r1,r2)
  gravitational_field_strength = (G * m)/(d**2)
  return gravitational_field_strength * r 
  pass


def main():
  pass
