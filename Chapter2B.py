# Angelo Smith
# 11/28/2022
# This Chapter is about print statements and quit statements
import MainCharacterA
import Chapter3C


def start():
    print("Zest stab wound has caused mutations in his body")
    print("Even though Zest escaped Angelo he's still weak")
    print("Four remnants of Zest family tries to kill you")
    Answer = int(input("What will you do 1. Kill your family 2. Beg your family not to kill you 3. Run away from your family"))
    if Answer == 1:
        print("Zest swiftly kills his family without a second thought and The knife becomes stronger")
    elif Answer == 3:
        print("As you run away from your family because of the sadness you felt from Angelo's massacre you cry")
        print("You tell yourself it's alright and move on")
    else:
        print("As you try to run away Angelo appears and kills your family and tear your limbs off")
        quit()
    Chapter3C.start()