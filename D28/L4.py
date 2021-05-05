class NamnSaknas(Exception):
    def __init__(self,message):
        print(message, "does not exist")

class Taget(Exception):
    def __init__(self,message):
        print(message, "already exists")


def create(dic,name):
    if name in dic:
        raise Taget(name)
    dic[name]=[]

def add(dic,name,nr):
    doesNameExist(dic,name)
    for person in dic:
        if nr in dic[person]:
            raise Taget(nr)
    dic[name].append(nr)

def lookup(dic, name):
    doesNameExist(dic,name)
    print("Numbers for", name + ":")
    for num in dic[name]:
        print(num)

def delete(dic,name,nr):
    doesNameExist(dic,name)
    dic[name].remove(nr)

def delete2(dic, name):
    doesNameExist(dic,name)
    dic.pop(name, None)

def doesNameExist(dic, name):
    if name not in dic:
        raise NamnSaknas(name)

def save(dic,file):
    f = open(file,'w')
    for contact in dic.items():
        f.write(contact[0] + ";")
        for num in contact[1]:
            f.write(num + ";")
        f.write("\n")
    f.close()

def load(dic,file):
    dic.clear()
    f = open(file,'r')
    for line in f:
        contact = line.split(";")
        contact.pop()
        dic[contact[0]] = contact[1:]
    f.close()

def run():
    dic = {}
    while True:
        inp = input("> ").split(" ")
        try:
            if inp[0] == "create":
                create(dic,inp[1])
            elif inp[0] == "add":
                add(dic,inp[1],inp[2])
            elif inp[0] == "lookup":
                lookup(dic,inp[1])
            elif inp[0] == "delete":
                if len(inp) == 2:
                    delete2(dic,inp[1])
                else:
                    delete(dic,inp[1],inp[2])
            elif inp[0] == "save":
                save(dic,inp[1])
            elif inp[0] == "load":
                load(dic,inp[1])
            elif inp[0] == "quit":
                break
        except NamnSaknas:
            pass
        except Taget:
            pass

run()
