class ListDictionary:
    def __init__(self):
        self.words=[]
        self.descs=[]

    def insert(self, word, desc):
        if word in self.words:
            raise NameError
        self.words.append(word)
        self.descs.append(desc)
    
    def lookup(self, word):
        for i in range(len(self.words)):
            if self.words[i]==word:
                return self.descs[i]
        raise NameError
