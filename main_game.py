#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame
import player
import blocks
import pyganim

WIN_WIDTH = 1024
WIN_HEIGHT = 768
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND = "#004400"
PF_WIDTH = PF_HEIGHT = 64

class Camera(object):
    
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    # Ограничения по границам
    l = min(0, l)                            # Не движемся дальше левой
    l = max(-(camera.width-WIN_WIDTH), l)    # Не движемся дальше правой
    t = max(-(camera.height-WIN_HEIGHT), t)  # Не движемся дальше нижней
    t = min(0, t)                            # Не движемся дальше верхней

    return pygame.Rect(l, t, w, h)

level = [
    "************************************",
    "*                                  *",
    "*      ***                         *",
    "*                         **********",
    "*                                  *",
    "*           *****                  *",
    "*                        ******    *",
    "*******                            *",
    "*                                  *",
    "*               **********         *",
    "*                                  *",
    "*                              *****",
    "*  **********                      *",
    "*                   *******        *",
    "*         ***                      *",
    "*                                  *",
    "************************************"
]
platforms = []
def main():
    pygame.init()

    hero = player.Player(100, 600)
    left = right = up = False

    entities = pygame.sprite.Group()
    entities.add(hero)

    timer = pygame.time.Clock()

    main_win = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("THE GAME")
    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(pygame.Color(BACKGROUND))

    total_level_width = len(level[0]) * PF_WIDTH
    total_level_height = len(level) * PF_HEIGHT

    camera = Camera(camera_configure, total_level_width, total_level_height)

    x = y = 0
    for row in level:
        for col in row:
            if col == "*":
                pf = blocks.Platform(x, y)
                entities.add(pf)
                platforms.append(pf)
            x += PF_WIDTH
        y += PF_HEIGHT
        x = 0

    done = True

    while done:
        timer.tick(30)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                done = False
            
            if e.type == pygame.KEYDOWN and e.key == pygame.K_LEFT:
                left = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RIGHT:
                right = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_UP:
                up = True

            if e.type == pygame.KEYUP and e.key == pygame.K_LEFT:
                left = False
            if e.type == pygame.KEYUP and e.key == pygame.K_RIGHT:
                right = False
            if e.type == pygame.KEYUP and e.key == pygame.K_UP:
                up = False
        
        bg.fill(pygame.Color(BACKGROUND))
        hero.update(left, right, up, platforms)
        camera.update(hero)
        for e in entities:
            bg.blit(e.image, camera.apply(e))
        #entities.draw(bg)
        main_win.blit(bg, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()