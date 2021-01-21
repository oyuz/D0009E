def bounce(n):
    print(n)
    if n==0:
        return
    bounce(n-1)
    print(n)

def bounce2(n):
    for i in range(n, 0, -1):
        print(i)
    for i in range(n+1):
        print(i)

def tvarsumman(n):
    if n//10==0:
        return n
    return n%10 + tvarsumman(n//10)

def tvarsumman2(n):
    tvarsumma=0
    while n!=0:
        tvarsumma += n%10
        n = n//10
    return tvarsumma 
