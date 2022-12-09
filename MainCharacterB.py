# Angelo Smith
# 11/28/2022
# This is what Angelo has his code
class MainCharacterB:


    def __init__(self, name, HP):
        self.name = name
        self.HP = HP
    def damage(self,damage):
        self.HP -= damage
        print("Damaged for",damage,"HP!")
name = "Angelo"
HP = 2
global Angelo
Angelo = MainCharacterB("Angelo", 2)