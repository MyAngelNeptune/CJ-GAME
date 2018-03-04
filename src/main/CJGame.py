import pygame
from pygame.locals import *

from src import *
from src.main.Charcters.Kaiyu import Kaiyu

from src.main.Scenes.SceneManager import SceneMananger
from src.main.Scenes.Menus.TitleScene import TitleScene
from src.main.Scenes.Menus.CharcterSelection import CharacterSelection
from src.main.Scenes.Button import Button


# Kill Ngrsda
# i want to dieh
# Nigge.
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
        selectionScreen = CharacterSelection()
        title = TitleScene()
        manager.go_to(CharacterSelection())
        active_sprite_list = pygame.sprite.Group()

        active_sprite_list.draw(screen)
        startButton = Button("Assets/Buttons/play.png", (727, 190), (400,125))
        title.render(screen)
        startButton.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
