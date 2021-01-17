import Uppgift1_4
import Uppgift5

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
            Uppgift1_4.bounce(n)

        elif inp==2:
            n = int(input("Enter parameter: "))
            print(Uppgift1_4.tvarsumman(n))

        elif inp==3:
            x = int(input("Enter x: "))
            print(Uppgift5.solve(Uppgift5.f1, x, 0.0001))

        elif inp==4:
            return

        else:
            print("Invalid input")
        
menu()
