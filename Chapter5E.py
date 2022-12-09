# Angelo Smith
# 11/28/2022
# This chapter is about the user fighting Angelo and random damage being hit to Angelo
import MainCharacterA
import MainCharacterB
import random

def start():
    print("Your HP is invigorated", MainCharacterA.Zest.HP)
    print("Zest has the Weapon to kill Angelo")
    print("Congratulations fool so you want to kill me")
    print("I only killed your family you can always make a new one kidding")
    print("What did I ever do to you?")
    print("I won't let you kill me")
    Answer = int(input("1. Fight 2.Pray before you fight 3.Leave"))
    if Answer == 1:
        print("Zest and Angelo both fight each other")
        print("Zest takes damage", MainCharacterA.Zest.damage(random.randint(2,4)))
        print("Zest hits Angelo but misses", MainCharacterB.Angelo.damage(0))
        MainCharacterB.Angelo.HP += 99
        print("Zest tries again and stabs Zest with his blade", MainCharacterB.Angelo.damage(random.randint(1,2)))
        print("Angelo gets angry and hits Zest with everything", MainCharacterA.Zest.damage(2))
        print("Zest smiles and say is that all you got and deals the finishing blow to head", MainCharacterB.Angelo.damage(99))
        print("He died and you won the battle!")
    elif Answer == 2:
        print("Zest prays and a divine spirit gives him MAX HP")
        MainCharacterA.Zest.HP += 99
        print("Zest Attacks and kills Angelo in one blow")
        print("With his last words being thank you")
    else:
        print("You decided that fighting Angelo is pointless and leave")
        print("As bitter as the fight was you felt sorry for him because he couldn't of made it this far without the help of others")
