def derivative(f, x, h):
    return (f(x+h)-f(x-h))/(2*h)

def solve(f, x0, h):
    x=x0-f(x0)/derivative(f,x0,h)
    if abs(x-x0)<h:
      return x
    return solve(f, x, h)
