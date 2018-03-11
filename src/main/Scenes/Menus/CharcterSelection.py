import pygame
class CharacterSelection(object):
    def __init__(self):
        super(CharacterSelection, self).__init__()

    def render(self, screen, events, manager):
        self.image = pygame.image.load("Assets/Screens/characterselection.png")
        self.image = pygame.transform.scale(self.image, (1200, 600))
        screen.blit(self.image, [0, 0])

    def update(self):
        pass

    def handle_events(self, events):
        pass