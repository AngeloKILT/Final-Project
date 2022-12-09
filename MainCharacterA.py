# Angelo Smith
# 11/3/2022
# This file is what the main character has

class MainCharacterA:
    Angelo_knife = 99

    def __init__(self, name, HP):
        self.name = name
        self.HP = HP
    def damage(self,damage):
        self.HP -= damage
        print("Damaged for",damage,"HP!")
name = "Zest"
HP = 2
global Zest
Zest = MainCharacterA("Zest", 2)
# global Ben #globalizes the variable Ben
