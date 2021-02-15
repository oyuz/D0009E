class Dictionary:
    def __init__(self):
        self.dic={}

    def insert(self, word, desc):
        self.dic[word]=desc

    def lookup(self, word):
        desc = self.dic.get(word)
        if desc == None:
            raise NameError
        else:
            return desc
