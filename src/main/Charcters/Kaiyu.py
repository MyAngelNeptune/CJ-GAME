import pygame
from src.main.Charcters.Character import Character

#Uses everything from character class
class Kaiyu(Character):
    def __init__(self):
        super().__init__()

        self.HP = 10000
        self.strength = 500
        self.agility = 740
        self.exp = 0
        self.x = 0
        self.y = 0

        self.image = pygame.image.load("Assets/Characters/kaiyu/Kaiyu.png")
        pygame.transform.scale(self.image, (300,300))
        # Fetch the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
