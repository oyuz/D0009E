class Board:
    def __init__(self, msg):
        self.message=msg


def main():
    b1 = Board("")
    b2 = Board("")
    kim = b1
    chris = b2
    while True:
        kimsBoard = getBoard(b1, b2, kim)
        chrisBoard = getBoard(b1, b2, chris)
        print("=== Bulletin board system ===")
        print("Kim reads message:", kimsBoard, ":", kim.message)
        print("Chris reads message:", chrisBoard, ":", chris.message)
        print("1: Direct Kim to other board")
        print("2: Direct Chris to other board")
        print("3: Tell Kim to post a message")
        print("4: Tell Chris to post a message")
        print("0: exit")
        inp = int(input("Enter choice: "))
        
        if inp==1:
            kim = changeBoard(b1, b2, kim)
        elif inp==2:
            chris = changeBoard(b1, b2, chris)
        elif inp==3:
            msg = input("Enter message for Kim to post: ")
            kim.message = kim.message + " " + msg
        elif inp==4:
            msg = input("Enter message for Chris to post: ")
            chris.message = chris.message + " " + msg
        elif inp==0:
            return
        else:
            print("Invalid alternative")

def getBoard(b1, b2, person):
    if person==b1:
        return "Board1"
    else:
        return "Board2"

def changeBoard(b1, b2, person):
    if person==b1:
        person = b2
    else:
        person = b1
    return person

main()
