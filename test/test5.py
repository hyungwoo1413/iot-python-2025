import pygame
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_SPACE, Rect
from pygame.draw import *
import sys

import random
import math

pygame.init()
Surface = pygame.display.set_mode((400, 400))
FPSCLOCK = pygame.time.Clock()
pygame.display.set_caption('Pygame Basic')
pygame.key.set_repeat(10, 10) # 키보드 연속 움직임 풀링

def main():
    is_game_start = False
    
    xpos = 200
    ypos = 200
    while True:
        Surface.fill(color='black')
        # Surface.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if event.type == KEYDOWN: # 키보드 입력이 시작되었으면
                if keys[pygame.K_LEFT]: # xpos - num
                    if xpos <= 5: xpos = 5
                    else: xpos -= 5
                if keys[pygame.K_RIGHT]:
                    if xpos >= 395: xpos = 395
                    else: xpos += 5
                if keys[pygame.K_UP]:
                    if ypos <= 5: ypos = 5
                    else: ypos -= 5
                if keys[pygame.K_DOWN]:
                    if ypos >= 395: ypos = 395
                    else: ypos += 5

        circle(Surface, (255,255,0), (xpos, ypos), 5)
        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__=='__main__':
    main()