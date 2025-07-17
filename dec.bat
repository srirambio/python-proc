def multiply(func):
  def sumofsquare(a,b):
    return func(a**2,b**3)
  return sumofsquare
@multiply
def add(x,y):
  return x + y
c=add(5,6)
print(c)

