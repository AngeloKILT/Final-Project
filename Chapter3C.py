# Angelo Smith
# 11/28/2022
# This chapter is mainly about Zest having health and taking damage
import MainCharacterA
import Chapter4D


def start():
    print("Your HP is", MainCharacterA.Zest.HP)
    MainCharacterA.Zest.HP = 1
    print("After Zest kills his family or runs away he is stopped by Angelo's Demon")
    print("The demon tells Zest he can revive his family but at a price")

# Since I'm still inexperienced at this coding I wanted the character to lose one HP and die at the 5th chapter
# ,but that will be done at the next chapter
    Answer = int(input("What will you do 1. Kill the Demon 2. Accept the Demon's offer"))
    if Answer == 1:
        print("Zest accepted the fact that there family is dead and smiled with the knife in hand and sliced it into "
              "piece's")
    else:
        print("Zest accepts the offer and loses one HP and see's his family again but Angelo kills them again with a smirk")
        print("With the stress of losing his family again and deceit of the demon Zest stabs himself with the knife")
        MainCharacterA.Zest.damage(1)
        print("Your HP is now",MainCharacterA.Zest.HP)
        if MainCharacterA.Zest.HP <= 0:
            print("You died!")
            quit()
    Chapter4D.start()
#start()