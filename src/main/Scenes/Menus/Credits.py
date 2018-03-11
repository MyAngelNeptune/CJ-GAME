import pygame
class Credits(object):
    def __init__(self):
        super(Credits, self).__init__()

    def render(self, screen):
        self.image = pygame.image.load("Assets/Screens/credits.png")
        self.image = pygame.transform.scale(self.image, (1200, 600))
        screen.blit(self.image, [0, 0])

    def update(self):
        pass

    def handle_events(self, events):
        pass