import pygame
from funcs import *


class Ball:
    def __init__(self, pos):
        self.radius = 5
        self.color = pygame.Color((255, 255, 255))
        self.plus_x = -1
        self.plus_y = -1
        self.x, self.y = pos
        self.delay = 10
        self.is_paused = False
        self.render()

    def move(self):
        if self.x - 10 == 0:
            self.plus_x = 1
        if self.x + 10 == screen_width:
            self.plus_x = -1
        if self.y - 10 == 0:
            self.plus_y = 1
        if self.y + 10 == screen_height:
            self.plus_y = -1
        self.x = self.x + self.plus_x
        self.y = self.y + self.plus_y

    def render(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)