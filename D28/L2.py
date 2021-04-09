import math

def logStar(n):
    counter = 0
    while(n>1):
        n = math.log(n,2)
        counter += 1
    return counter

import d0028e_lab2_logStarTest

def tvarsumman(n):
    Sum = 0
    while(n>0):
        Sum += n%10
        n = n // 10
    return Sum

import d0028e_lab2_sumTest

def avbetalningsplan(skuld,sats,belopp):
    print("Årling avbetalning:", belopp)
    print("Räntesats:", sats, "%")
    print("Ingående skuld:", skuld, "\n")
    
    year = 0

    while(skuld > 0):
        year+=1
        interest = skuld * sats
        amortizedAmount = belopp - interest
        
        if (skuld - amortizedAmount >= 0):
            skuld -= amortizedAmount
        else:
            amortizedAmount = skuld
            skuld = 0

        print("-- År", year, "--")
        print("Återstående skuld:", skuld)
        print("Amorterat belopp:", amortizedAmount)
        print("Ränta", interest, "\n")

avbetalningsplan(100,0.05,25)


def derivative(f, x, h):
    return (f(x+h)-f(x-h))/(2*h)

def solve(f, x0, h):
  while True:
    x=x0-f(x0)/derivative(f,x0,h)
    if abs(x-x0)<h:
      return x
    x0=x

import d0028e_lab2_solveTest
