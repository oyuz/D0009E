def derivative(f, x, h):
    return (f(x+h)-f(x-h))/(2*h)

def solve(f, x0, h):
  while True:
    x=x0-f(x0)/derivative(f,x0,h)
    if abs(x-x0)<h:
      return x
    x0=x

def f1(x):
    return x**2-1

def f2(x):
    return 2**x-1 
