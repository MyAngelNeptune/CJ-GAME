import pygame

#A generic super class level
class Level():

    #Constructor to pass in a player
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when moving
            platforms collide with the player. """