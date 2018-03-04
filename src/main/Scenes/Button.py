import pygame


class Button(object):

    def __init__(self, fileLocation,  position, size):

        self.image = pygame.image.load(fileLocation)
        self.size = size
        self.image = pygame.transform.scale(self.image, size)
        # get image size and position
        self.position = position
        self.rect = self.image.get_rect()
        print(self.size)

    def draw(self, screen):
        # draw selected image
        screen.blit(self.image, self.position)

#    def event_handler(self, event):
#        if event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
 #           if event.button == 1: # is left button clicked
                #if self._rect.collidepoint(event.pos): # is mouse over button
