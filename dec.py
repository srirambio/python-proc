def mul(func):
  def sumofsquare(a,b):
    return func(a**2,b**3)
  return sumofsquare
@mul    
def fun(x,y):
  return x + y
c=fun(5,6)
print(c)

