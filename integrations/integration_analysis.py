import numpy as np
from simpsons import simpsons_integration
from simple import simple_integration
"""
Test known integrals, with variable dx belonging to 
Moon period is 2358720s. 1s of this is 0.000042% of the orbit. We test with dx

[0.000042, 0.00042, 0.0042, 0.042] (%). 

----
1. Straight lines
2. Quadratics
3. Exponentials
4. Ellipses

1. Straight line examples
y = x [0<x<10], Expected area: 5

2. Quadratics
y = x^2 [0<x<10]

3. Exponentials
y = e^x [0<x<10]

4. Sine wave
y = sin(x) [0<x<10]

"""

class TestIntegrationMethods:
  def __init__(self):
    self.a = 0
    self.b = 10
    self.areas = {
      "straight_line": 50,
      "quadratics": 1000/3,
      "exponentials": np.exp(10)-np.exp(1),
      "Sine": np.cos(0)-np.cos(10)
    }
    self.dx = np.array([4.24e-7, 4.24e-6, 4.24e-5, 4.24e-4])*(self.b-self.a) #dx
    self.n = np.array([np.int64((self.b-self.a)//dx_i) for dx_i in self.dx]) #no. of partitions
    self.xs = [np.linspace(self.a,self.b,n) for n in self.n] #x values of equal width
  def straight_lines_func(self,x):
    return x
  def quadratic_func(self,x,a=1,b=0,c=0):
    return a*x**2 + b*x + c
  
  def exponentials_func(self,x):
    return np.exp(x)
  def sine_func(self,x):
    return np.sin(x)
  def integral_test(self, integral_method, f):
    total_area = 0
    for i in range(0,len(self.xs[0])-1):
      x0 = self.xs[0][i]
      x2 = self.xs[0][i+1] #TODO change back index to j for looping through intervals
      total_area += integral_method(f,x0,x2)
    return total_area
  
  def get_areas(self, line):
    simpsons_area = self.integral_test(simpsons_integration, line)
    simple_area = self.integral_test(simple_integration, line)
    return {"simple" : simple_area, "simpsons" : simpsons_area}
  
  def main(self):
    comparisons = []
    for method in [self.straight_lines_func, self.quadratic_func,self.exponentials_func, self.sine_func]:
      comparisons.append(self.get_areas(method))
    return comparisons

test = TestIntegrationMethods()

print(test.main())
