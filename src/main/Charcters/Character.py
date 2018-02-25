import pygame

#Get to use everything from sprite class
class Character(pygame.sprite.Sprite):
    def __init__(self):
        self.HP = ""
        self.strength = ""
        self.agility = ""
        self.exp = ""
        self.x = 100
        self.y = 100

        #Calls the parent class (sprite) constructor
        super().__init__()
