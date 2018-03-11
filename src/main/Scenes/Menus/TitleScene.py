import pygame
from src.main.Scenes.Scene import Scene
class TitleScene(Scene):
    def __init__(self):
        super(TitleScene, self).__init__()

    def render(self, screen):
        self.image = pygame.image.load("Assets/Screens/Title.png")
        self.image = pygame.transform.scale(self.image, (1200, 600))
        screen.blit(self.image, [0, 0])

    def update(self):
        pass

    def handle_events(self, events, scene):
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    self.manager.go_to(scene)