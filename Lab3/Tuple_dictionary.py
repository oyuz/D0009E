class TupleDictionary:
    def __init__(self):
        self.dic=[]

    def insert(self, word, desc):
        for tup in self.dic:
            if tup[0]==word:
                raise NameError
        self.dic.append((word,desc))

    def lookup(self, word):
        for tup in self.dic:
            if tup[0]==word:
                return tup[1]
        raise NameError
