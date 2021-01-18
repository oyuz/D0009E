class Number:
    def __init__(self, number):
        self.number = number

    def getNumber(self):
        return self.number

    def setNumber(self, number):
        self.number = number
    

class Telefonbok:
    def __init__(self):
        self.dic = {}
        self.cmd = {
            "add" : self.add,
            "lookup" : self.lookup,
            "alias" : self.alias,
            "change" : self.change,
            "save" : self.save,
            "load" : self.load,
            "quit" : self.quit
            }
        self.prompt()
        

    def prompt(self):
        while True:
            inp = input(("telebok> ")).split()
            try:
                self.cmd[inp[0]](*inp[1:])
            except TypeError:
                print("Invalid command")
            except SystemExit:
                return
            
    def add(self, name, number):
        if name in self.dic:
            print(name, "already exists")
        if self.number_available(number):
            self.dic[name] = Number(number)
    
    def lookup(self, name):
        try:
            print(self.dic[name].getNumber())
        except KeyError:
            print(name, "not found")

    def alias(self, name, alias):
        if alias in self.dic or name not in self.dic:
            print("name not found or duplicate name")
        else:
            self.dic[alias] = self.dic[name]

    def change(self, name, number):
        if self.number_available(number):
            self.dic[name].setNumber(number)

    def number_available(self, number):
        for num in self.dic.values():
            if num.getNumber() == number:
                print(number, "already exists")
                return False
        return True

    def save(self, file):
        f = open(file, 'w')
        for contact in self.dic.items():
            f.write(contact[1].getNumber() + ";" + contact[0] + ";" + "\n")
        f.close()

    def load(self, file):
        f = open(file, 'r')
        for line in f:
            contact = line.split(";")
            self.add(contact[1], contact[0])
        f.close()

    def quit(self):
        raise SystemExit

t = Telefonbok()
