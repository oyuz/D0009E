class OccupiedException(Exception):
    def __init__(self, message):
        print(message, "already exists")
        

class NotFoundException(Exception):
    def __init__(self, message):
        print(message, "not found")
        

class AliasException(Exception):
    def __init__(self):
        print("name not found or duplicate name")


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

    def add(self, name, number):
        if name in self.dic:
            raise OccupiedException(name)
        if not self.number_available(number):
            raise OccupiedException(number)
        self.dic[name] = Number(number)
              
    def number_available(self, number):
        for num in self.dic.values():
            if num.getNumber() == number:
                return False
        return True

    def lookup(self, name):
        try:
            print(self.dic[name].getNumber())
        except KeyError:
            raise NotFoundException(name)

    def alias(self, name, alias):
        if alias in self.dic or name not in self.dic:
            raise AliasException
        self.dic[alias] = self.dic[name]

    def change(self, name, number):
        if name not in self.dic:
            raise NotFoundException(name)
        if not self.number_available(number):
            raise OccupiedException(number)
        self.dic[name].setNumber(number)

    def save(self, file):
        f = open(file, 'w')
        for contact in self.dic.items():
            f.write(contact[1].getNumber() + ";" + contact[0] + ";" + "\n")
        f.close()

    def load(self, file):
        self.dic.clear()
        f = open(file, 'r')
        for line in f:
            contact = line.split(";")
            self.add(contact[1], contact[0])
        f.close()

    def quit(self):
        raise SystemExit
            

class TelefonbokUI:
    def __init__(self):
        self.book = Telefonbok()
        self.cmd = {
            "add" : self.book.add,
            "lookup" : self.book.lookup,
            "alias" : self.book.alias,
            "change" : self.book.change,
            "save" : self.book.save,
            "load" : self.book.load,
            "quit" : self.book.quit
            }

    def run(self):
        while True:
            inp = input(("telebok> ")).split()
            try:
                self.cmd[inp[0]](*inp[1:])
            except TypeError:
                print("Invalid command")
            except IndexError:
                print("Invalid command")
            except KeyError:
                print("Invalid command")
            except OccupiedException:
                pass
            except NotFoundException:
                pass
            except AliasException:
                pass
            except SystemExit:
                return

def main():
    tui = TelefonbokUI()
    tui.run()

if __name__ == "__main__":
    main()
