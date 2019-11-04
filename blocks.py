#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame

PF_WIDTH = PF_HEIGHT = 64
PF_COLOR = "#FF6262"

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((PF_WIDTH, PF_HEIGHT))
        self.image = pygame.image.load("tiles/bricks/005.png")
        self.rect = pygame.Rect(x, y, PF_WIDTH, PF_HEIGHT)