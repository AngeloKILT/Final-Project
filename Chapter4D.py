# Angelo Smith
# 11/28/2022
# In this chapter the user gains health and loses it.
# The code also has a while statement for talking to the enemy.
# There is also a for loop statement as well.
import MainCharacterA
import Chapter5E


def start():
    print("Your HP is", MainCharacterA.Zest.HP)
    print("Zest reaches Angelo and only has one HP")
    print("Angelo is worried about dying so he tries to make Zest lose a life in the final battle")
    print("Zest is too weak to fight Angelo and needs HP")
    Answer = int(input("What will you do 1.Eat a fruit to get HP 2. Talk to Angelo 3. Fight Angelo"))
    if Answer == 1:
        print(" Zest finds a fruit of HP it was hearty but had some spikes inside that damage Zest")
        MainCharacterA.Zest.HP += 30
        print("Your HP is invigorated", MainCharacterA.Zest.HP)
        MainCharacterA.Zest.damage(27)
        print("I can't let you overpower me that easily fool and your HP is", MainCharacterA.Zest.HP)
    elif Answer == 2:
        print("You decided to talk to Angelo with a sense of respect because you know he may kill you")
        print("He tells you he doesn't want to die and this game's creator is cruel")
        print("You have unlocked a secret choice")
        stop_talking = False
        while stop_talking == False:
            topic = input(" 1.Why did you kill my family? 2. Who created you? 3.Is this really the end?")
            if topic == "1":
                print("I didn't want to kill them I was told to and I will not give any details why")
            elif topic == "2":
                print("I was created by a person who exist outside our world")
            elif topic == "3":
                print("I don't know what you mean by that and you're starting to annoy me")
                stop_talking = True
            else:
                print("If your going to keep speaking nonsense I will just leave Later!")

    else:
        print("You try to fight Angelo but  he look's nervous")
        print("He says your a fool trying to speak to me")
        print("You raise your fist at him and see it gone while you look at him")
        for (i) in range(9):
            print("You blackout and notice your heart on the floor and hear someone laughing")
            print("you are now stuck in this loop for trying to fight a powerful being")
        quit()
    Chapter5E.start()
