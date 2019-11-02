#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame
import player

WIN_WIDTH = 640
WIN_HEIGHT = 480
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND = "#004400"


PF_WIDTH = PF_HEIGHT = 32
PF_COLOR = "#FF6262"

level = [
    "********************",
    "*                  *",
    "*                  *",
    "*      ***         *",
    "*                  *",
    "*                  *",
    "*                  *",
    "*        ****      *",
    "*                  *",
    "*                  *",
    "*  **********      *",
    "*                  *",
    "*           *      *",
    "*                  *",
    "********************"
]

def main():
    pygame.init()

    timer = pygame.time.Clock()

    main_win = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("THE GAME")
    bg = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
    bg.fill(pygame.Color(BACKGROUND))

    hero = player.Player(55, 55)
    left = right = up = False

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
        x = y = 0
        for row in level:
            for col in row:
                if col == "*":
                    pf = pygame.Surface((PF_WIDTH, PF_HEIGHT))
                    pf.fill(pygame.Color(PF_COLOR))
                    bg.blit(pf, (x, y))
                x += PF_WIDTH
            y += PF_HEIGHT
            x = 0

        hero.update(left, right, up)
        hero.draw(bg)
        main_win.blit(bg, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()