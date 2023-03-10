import pygame
from funcs import *
import random


class Square:
    def __init__(self, coords, length):
        self.x, self.y = coords
        self.x_end = self.x + length
        self.y_end = self.y + length
        self.length = length
        self.rect = pygame.Rect(self.x, self.y, self.length, self.length)

    def get_coords(self):
        return (self.x, self.y)

