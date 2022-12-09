# Angelo Smith
# 11/28/2022
# This chapter is about the user inputting  a number and progressing through the game.
# The if statements are meant for choices
import MainCharacterA
import Chapter2B


def start():
    #print("Ben's name is ",MainCharacterA.Ben.name) #Should print "Angelo" this time
    print("Angelo is a murderer who killed your family!")
    print("You are known as Zest a person who witnessed this murder")
    print("Angelo spots you and stabs you")
    print(MainCharacterA.Zest.HP)
    MainCharacterA.Zest.HP += 5
    Answer = int(input("What will you do 1.Go forward  2.Attack  3.Escape 4.Death"))
    if Answer == 1:
        print("Zest moves forward and pulls the knife out.")
        print("Zest aura of determination has moved him to the next part")
    elif Answer == 3:
        print("Zest decides to escape Angelo")
        print("However Zest is overwhelmed and escapes with the feeling of weakness")
    else:
        print("You are killed by Angelo for being weak and/or for giving up")
        quit()

    Chapter2B.start()
