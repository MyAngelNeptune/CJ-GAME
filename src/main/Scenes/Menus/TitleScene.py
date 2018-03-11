import pygame
from src.main.Scenes.Scene import Scene
from src.main.Scenes.Button import Button
import src.main.Scenes.SceneManager
from src.main.Scenes.Menus.CharcterSelection import CharacterSelection
from src.main.Scenes.Menus.Credits import Credits
class TitleScene(Scene):
    def __init__(self):
        super(TitleScene, self).__init__()

    def render(self, screen, events, manager):
        self.image = pygame.image.load("Assets/Screens/Title.png")
        self.image = pygame.transform.scale(self.image, (1200, 600))

        screen.blit(self.image, [0, 0])

        startButton = Button("Assets/Buttons/play.png", (727, 50), (400, 125))

        startButton.draw(screen)

        creditsButton = Button("Assets/Buttons/credits.png", (727, 190), (400, 125))
        creditsButton.draw(screen)

        quitButton = Button("Assets/Buttons/quit.png", (727, 330), (400, 125))
        quitButton.draw(screen)

        selectionScreen = CharacterSelection()
        CreditsScreen = Credits()

        #Checks if the start button was clicked
        if(startButton.event_handler(events)):
            manager.go_to(selectionScreen)
            manager.scene.render(screen, events, manager)
            pygame.display.flip()

        elif(creditsButton.event_handler(events)):
            manager.go_to(CreditsScreen)
            manager.scene.render(screen, events, manager)

        #Checks if the quit button was clicked
        elif(quitButton.event_handler(events)):
            pygame.quit()
        pygame.display.flip()


    def update(self):
        pass

    def handle_events(self, events, scene):
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    self.manager.go_to(scene)