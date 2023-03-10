import pygame
from funcs import *
import random


class Ball:
    def __init__(self, start, pos, screen, screen_size):
        self.radius = 10
        self.speed = 1
        self.count_of_hit_board = 0
        self.can_change_y = False
        self.sin = get_sin(start, pos)
        self.cos = get_cos(start, pos)
        self.color = pygame.Color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.plus_x, self.plus_y = self.cos * self.speed, self.sin * self.speed
        self.x, self.y = start
        self.screen = screen
        self.screen_width, self.screen_height = screen_size
        self.render()

    def get_coords(self):
        return (self.x, self.y)

    def move(self, y_of_board, squares):
        if self.x + self.radius >= self.screen_width or self.x <= 0:
            self.plus_x = -self.plus_x
        if self.y + self.radius < y_of_board:
            self.can_change_y = True
        if self.y + self.radius >= y_of_board and self.can_change_y:
            self.y = y_of_board - 2 * self.radius
            self.plus_y = -self.plus_y
        if self.y <= 0:
            self.plus_y = -self.plus_y
        for square in squares:
            if square.rect.collidepoint(self.x + self.radius * (self.plus_x / abs(self.plus_x)) + self.plus_x, self.y):
                self.plus_x = -self.plus_x
            if square.rect.collidepoint(self.x, self.y + self.plus_y + self.radius * (self.plus_y / abs(self.plus_y))):
                self.plus_y = -self.plus_y
        self.x = self.x + self.plus_x
        self.y = self.y + self.plus_y

    def render(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)