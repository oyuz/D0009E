class Dictionary:
    def __init__(self):
        self.dic={}

    def insert(self, word, desc):
        if word in self.dic:
            raise NameError
        self.dic[word]=desc

    def lookup(self, word):
        desc = self.dic.get(word)
        if desc == None:
            raise NameError
        else:
            return desc
