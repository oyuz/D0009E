class TupleDictionary:
    def __init__(self):
        self.dic=[]

    def insert(self, word, desc):
        self.dic.append((word,desc))

    def lookup(self, word):
        for tup in self.dic:
            if tup[0]==word:
                print("Description for", word, ":", tup[1])
                return
        raise NameError
