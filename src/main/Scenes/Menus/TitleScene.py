import pygame
class TitleScene(object):
    def __init__(self):
        super(TitleScene, self).__init__()

    def render(self, screen):
        self.image = pygame.image.load("Assets/Screens/Title.png")

    def update(self):
        pass

    def handle_events(self, events):
        pass