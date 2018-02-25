import pygame
from src.main.Charcters import Character

#Uses everything from character class
class Kaiyu(pygame.sprite.Sprite):
    def __init__(self):
        self.HP = 10000
        self.strength = 500
        self.agility = 740
        self.exp = 0
        self.x = 0
        self.y = 0

        self.image = pygame.image.load("Assets/Characters/kaiyu/Kaiyu.png")
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        super().__init__()

