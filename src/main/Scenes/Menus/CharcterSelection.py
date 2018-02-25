import pygame
class CharacterSelection(object):
    def __init__(self):
        super(CharacterSelection, self).__init__()

    def render(self, screen):
        self.image = pygame.image.load("Assets/Screens/characterselection.png")
        screen.blit(self.image)

    def update(self):
        pass

    def handle_events(self, events):
        pass