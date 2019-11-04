#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame
import player
import blocks
import pyganim

WIN_WIDTH = 1280
WIN_HEIGHT = 832
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND = "#004400"
PF_WIDTH = PF_HEIGHT = 64

level = [
    "********************",
    "*                  *",
    "*      ***         *",
    "*                  *",
    "*                  *",
    "*           *****  *",
    "*                  *",
    "*                  *",
    "*  **********      *",
    "*                  *",
    "*         ***      *",
    "*                  *",
    "********************"
]
platforms = []
def main():
    pygame.init()

    hero = player.Player(100, 100)
    left = right = up = False

    entities = pygame.sprite.Group()
    entities.add(hero)

    timer = pygame.time.Clock()

    main_win = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("THE GAME")
    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(pygame.Color(BACKGROUND))

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
        entities.draw(bg)
        main_win.blit(bg, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()