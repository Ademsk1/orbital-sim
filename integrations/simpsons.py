def simpsons_integration(f, a,b):
  estimated_area = (f(a) + 4*f((a+b)/2) + f(b)) * (b-a)/6
  return estimated_area

# class myTest:
#   def test_function(self,x):
#     return x

# test = myTest()
# print(simpsons_integration(test.test_function, 1,2))
