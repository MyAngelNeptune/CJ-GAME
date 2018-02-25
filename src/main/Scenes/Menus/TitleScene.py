import pygame
class TitleScene(object):
    def __init__(self):
        super(TitleScene, self).__init__()

    def render(self, screen):
        self.image = pygame.image.load("Assets/Screens/Title.png")
        self.image = pygame.transform.scale(self.image, (1200, 600))
        screen.blit(self.image, [0, 0])

    def update(self):
        pass

    def handle_events(self, events):
        pass