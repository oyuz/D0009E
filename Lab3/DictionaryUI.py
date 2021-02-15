import List_dictionary
import Tuple_dictionary
import Dictionary

class DictionaryUI:
    def run(self):
        print("\nSelect dictionary data structure: \n")
        print("1: Lists")
        print("2: List containing tuples")
        print("3: Dictionary \n")
        inp=int(input("Choose alternative: "))
        
        if inp==1:
            listDictionary=List_dictionary.ListDictionary()
            self.menu(listDictionary)
            
        elif inp==2:
            tupleDictionary=Tuple_dictionary.TupleDictionary()
            self.menu(tupleDictionary)
            
        elif inp==3:
            dictionary=Dictionary.Dictionary()
            self.menu(dictionary)
            
        else:
            raise Exception("Invalid input")
        
        
    def menu(self, dictionary):
        while True:
            print("\nMenu for dictionary \n")
            print("1: Insert")
            print("2: Lookup")
            print("3: Exit program \n")
            inp=int(input("Choose alternative: "))
            
            if inp==1:
                word = input("Word to insert: ")
                desc = input("Description of word: ")
                dictionary.insert(word, desc)

            elif inp==2:
                word = input("Word to lookup: ")
                try:
                    desc = dictionary.lookup(word)
                    print("Description for", word, ":", desc)
                except NameError:
                    print(word, "cannot be found in the dictionary")

            elif inp==3:
                return

            else:
                print("Invalid input")

def main():
    dui = DictionaryUI()
    dui.run()

if __name__ == "__main__":
    main()
