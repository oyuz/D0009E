import U1_4
import U5

def menu():
    while True:
        print("This is a menu for lab 2,",
              "choose one of the following alternatives:")
        print("1. Enter a parameter for bounce to run")
        print("2. Enter a parameter for digit sum to run")
        print("3. Enter an initial x value for newton-raphson to",
              "be run on f(x)=x^2-1")
        print("4. Exit menu")
        inp = int(input("Enter alternative: "))

        if inp==1:
            n = int(input("Enter parameter: "))
            U1_4.bounce(n)

        elif inp==2:
            n = int(input("Enter parameter: "))
            print(U1_4.tvarsumman(n))

        elif inp==3:
            x = int(input("Enter x: "))
            print(U5.solve(U5.f1, x, 0.0001))

        elif inp==4:
            return

        else:
            print("Invalid input")
        
menu()
