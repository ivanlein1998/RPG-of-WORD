import random
class style:
    def __init__(self, attack, defence, health, speed):
        self.attack = attack
        self.defence = defence
        self.health = health
        self.speed = speed

class shielder(style):
    def __init__(self, attack, defence, health, speed):
        super().__init__(10, 50, 200, 10)

class assassin(style):
    def __init__(self, attack, defence, health, speed):
        super().__init__(50, 5, 100, 50)

class archer(style):
    def __init__(self, attack, defence, health, speed):
        super().__init__(30, 10, 150, 35)

class saber(style):
    def __init__(self, attack, defence, health, speed):
        super().__init__(40, 20, 200, 20)

class Character:
    def __init__(self, name, style, level, experience):
        self.name = name
        self.style = style
        self.level = 1
        self.experience = 0
    def gainExperience(amount):
        experience += amount
        level = getLevel(experience)

def getLevel(experience):
    for x in range (level):
        if (experience-(level*1.1*100)
name = input("what is your name")
PlayerClass = input 
