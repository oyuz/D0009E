def menu():
    print("Menu for dictionary")
    print("1: Insert")
    print("2: Lookup")
    print("3: Exit program")

def dictionary():
    dic = {}
    while True:
        menu()
        inp = int(input(("Choose alternative: ")))
        
        if inp==1:
            word = input("Word to insert: ")
            desc = input("Description of word: ")
            insertDic(dic, word, desc)

        elif inp==2:
            word = input("Word to lookup: ")
            lookupDic(dic, word)

        elif inp==3:
            return

        else:
            print("Invalid input")

def insertDic(dic, word, desc):
    dic[word] = desc

def lookupDic(dic, word):
    desc = dic.get(word)
    if desc == None:
        raise Exception("Word:", word, "cannot be found in the dictionary")
    else:
        print("Description for", word, ":", dic.get(word))

def tuples():
    Arr = []
    while True:
        menu()
        inp = int(input(("Choose alternative: ")))
        
        if inp==1:
            word = input("Word to insert: ")
            desc = input("Description of word: ")
            insertTup(Arr, word, desc)

        elif inp==2:
            word = input("Word to lookup: ")
            lookupTup(Arr, word)

        elif inp==3:
            return

        else:
            raise Exception("Invalid input")

def insertTup(Arr, word, desc):
    Arr.append((word, desc))

def lookupTup(Arr, word):
    for tup in Arr:
        if tup[0]==word:
            print("Description for", word, ":", tup[1])
            return
    raise Exception("Word:", word, "cannot be found in the dictionary")

        
def lists():
    wordArr = []
    descArr = []
    while True:
        menu()
        inp = int(input(("Choose alternative: ")))
        
        if inp==1:
            word = input("Word to insert: ")
            desc = input("Description of word: ")
            insertArr(wordArr, descArr, word, desc)

        elif inp==2:
            word = input("Word to lookup: ")
            lookupArr(wordArr, descArr, word)

        elif inp==3:
            return

        else:
            raise Exception("Invalid input")

def insertArr(wordList, descList, word, desc):
    wordList.append(word)
    descList.append(desc)

def lookupArr(wordArr, descArr, word):
    for i in range(len(wordArr)):
        if wordArr[i] == word:
            print("Description for", word, ":", descArr[i])
            return
    raise Exception("Word:", word, "cannot be found in the dictionary")
