class ListDictionary:
    def __init__(self):
        self.words=[]
        self.descs=[]

    def insert(self, word, desc):
        self.words.append(word)
        self.descs.append(desc)
    
    def lookup(self, word):
        for i in range(len(self.words)):
            if self.words[i]==word:
                print("Description for", word, ":", self.descs[i])
                return
        raise NameError
