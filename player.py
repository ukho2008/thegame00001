#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame

MOVE_SPEED = 7
JUMP_POWER = 10
GRAVITY = 0.35
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.on_ground = False
        self.image = pygame.Surface((WIDTH, HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)

    def update(self, left, right, up):
        if left:
            self.xvel = -MOVE_SPEED

        if right:
            self.xvel = MOVE_SPEED

        if not (left or right):
            self.xvel = 0

        if up:
            if self.on_ground:
                self.yvel = -JUMP_POWER
        
        if not self.on_ground:
            self.yvel += GRAVITY

        self.on_ground = False

        self.rect.x += self.xvel
        self.rect.y += self.yvel

    def draw(self, bg):
        bg.blit(self.image, (self.rect.x, self.rect.y))