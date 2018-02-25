import pygame
from pygame.locals import *

from src.main.Scenes.SceneManager import SceneMananger
#Kill Ngrsda
#i want to dieh
DISPLAY = 1200, 600
DEPTH = 0
FLAGS = 0
def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("DEATH GAME")
    timer = pygame.time.Clock()
    running = True

    manager = SceneMananger()

    while running:
        timer.tick(60)

        if pygame.event.get(QUIT):
            running = False
            return
        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()