import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_SPACE, Rect
from pygame.draw import *
import sys
import random

DISPLAY = 400
HERO_SIZE = 3
HERO_SPEED = 5
MONSTER_SIZE = 5
MONSTER_SPEED = 0.3

class Monster:
    def __init__(self):
        pass

    def move(self):
        pass

class Galaxy:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((DISPLAY, DISPLAY))
        pygame.display.set_caption('Pygame Basic')
        pygame.key.set_repeat(10, 10) # 키보드 연속 움직임 풀링
        self.clock = pygame.time.Clock()
        self.xpos = 200
        self.ypos = 200
        self.is_game_start = False 
    
    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                self.keydown()

    def keydown(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            if self.xpos <= HERO_SIZE:
                self.xpos = HERO_SIZE
            else:
                self.xpos -= HERO_SPEED
        if keys[K_RIGHT]:
            if self.xpos >= DISPLAY-HERO_SIZE:
                self.xpos = DISPLAY-HERO_SIZE
            else:
                self.xpos += HERO_SPEED
        if keys[K_UP]:
            if self.ypos <= HERO_SIZE:
                self.ypos = HERO_SIZE
            else:
                self.ypos -= HERO_SPEED
        if keys[K_DOWN]:
            if self.ypos >= DISPLAY-HERO_SIZE:
                self.ypos = DISPLAY-HERO_SIZE
            else:
                self.ypos += HERO_SPEED

    def update(self):
        self.surface.fill('black')
        circle(self.surface, (255, 255, 0), (self.xpos, self.ypos), HERO_SIZE)

        pygame.display.update()

    def run(self):
        while True:
            self.event()
            self.update()
            self.clock.tick(1000)


if __name__ == '__main__':
    game = Galaxy()
    game.run()