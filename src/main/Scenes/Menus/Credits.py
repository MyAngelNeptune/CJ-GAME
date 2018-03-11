import pygame
from src.main.Scenes.Button import Button
class Credits(object):
    def __init__(self):
        super(Credits, self).__init__()

    def render(self, screen, events, manager):
        self.image = pygame.image.load("Assets/Screens/creditpage.png")
        self.image = pygame.transform.scale(self.image, (1200, 600))
        screen.blit(self.image, [0, 0])

        returnButton = Button("Assets/Buttons/return.png", (600.727, 727-300), (300, 95))
        returnButton.draw(screen)

    def update(self):
        pass

    def handle_events(self, events):
        pass