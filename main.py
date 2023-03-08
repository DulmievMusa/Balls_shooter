import pygame
from objects.ball import Ball
from funcs import *
MYEVENTTYPE = pygame.USEREVENT + 1
balls_sp = []


def draw_line(pos):
    if pos[1] >= screen_height - 100 or pos == [10000000000, 10000000]:
        return
    k, b = get_k_and_b([x0, y0], pos)
    final = (-b // k, 0)
    pygame.draw.line(screen, pygame.Color("white"), (x0, y0), final)


def spawn_balls(pos):
    pass


if __name__ == '__main__':
    pygame.init()
    screen_size = screen_width, screen_height = 1000, 1000
    screen = pygame.display.set_mode(screen_size)
    screen.fill(pygame.Color('black'))
    running = True
    clock = pygame.time.Clock()
    yes = False
    pos = [10000000000, 10000000]
    x0 = screen_width // 2
    y0 = screen_height - 100
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        clock.tick(600)
        pygame.display.flip()
        screen.fill(pygame.Color('black'))
        draw_line(pos)
    pygame.quit()