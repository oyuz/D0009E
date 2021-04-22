def menu():
    print("Menu for dictionary \n 1: Insert \n 2: Lookup \n 3: Exit program")

def dic1():
    a = []
    b = []
    while True:
        menu()
        inp = int(input("Choose alternative: "))
        if inp == 1:
            wrd = input("Word to insert: ")
            if wrd in a:
                print("Word already exists")
            else:
                dsc = input("Description of word: ")
                ins1(wrd,dsc,a,b)
        elif inp == 2:
            lkp = input("Word to lookup: ")
            lookup1(lkp,a,b)
        elif inp == 3:
            break

def ins1(wrd,dsc,a,b):
    a.append(wrd)
    b.append(dsc)

def lookup1(lkp,a,b):
    for i in range(len(a)):
        if a[i] == lkp:
            print("Description for", lkp + ":", b[i])
            return
    print("Word does not exist")

def dic2():
    a = []
    while True:
        menu()
        inp = int(input("Choose alternative: "))
        if inp == 1:
            wrd = input("Word to insert: ")
            if any(wrd in tup for tup in a):
                print("Word already exists")
            else:
                dsc = input("Description of word: ")
                ins2(wrd,dsc,a)
        elif inp == 2:
            lkp = input("Word to lookup: ")
            lookup2(lkp,a)
        elif inp == 3:
            break

def ins2(wrd,dsc,a):
    a.append((wrd,dsc))

def lookup2(lkp,a):
    for tup in a:
        if tup[0] == lkp:
            print("Description for", lkp + ":", tup[1])
            return
    print("Word does not exist")

def dic3():
    a = {}
    while True:
        menu()
        inp = int(input("Choose alternative: "))
        if inp == 1:
            wrd = input("Word to insert: ")
            if wrd in a:
                print("Word already exists")
            else:
                dsc = input("Description of word: ")
                ins3(wrd,dsc,a)
        elif inp == 2:
            lkp = input("Word to lookup: ")
            lookup3(lkp,a)
        elif inp == 3:
            break

def ins3(wrd,dsc,a):
    a[wrd] = dsc

def lookup3(lkp,a):
    if lkp not in a:
        print("Word does not exist")
    else:
        print("Description for", lkp + ":", a[lkp])

#dic1()
#dic2()
dic3()
