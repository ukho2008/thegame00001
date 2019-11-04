#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pygame
import pyganim

MOVE_SPEED = 7
JUMP_POWER = 13
GRAVITY = 0.35
WIDTH = 64
HEIGHT = 64
COLOR = "#00ff00"

ANIMATION_DELAY      = 0.1
ANIMATION_RIGHT      = [("tiles/predator/walk_R-01.png"),
                        ("tiles/predator/walk_R-02.png"),
                        ("tiles/predator/walk_R-03.png"),
                        ("tiles/predator/walk_R-04.png"),
                        ("tiles/predator/walk_R-05.png"),
                        ("tiles/predator/walk_R-06.png")]
ANIMATION_LEFT       = [("tiles/predator/walk_L-01.png"),
                        ("tiles/predator/walk_L-02.png"),
                        ("tiles/predator/walk_L-03.png"),
                        ("tiles/predator/walk_L-04.png"),
                        ("tiles/predator/walk_L-05.png"),
                        ("tiles/predator/walk_L-06.png")]
ANIMATION_JUMP_RIGHT = [("tiles/predator/jump_R.png", 0.1)]
ANIMATION_JUMP_LEFT  = [("tiles/predator/jump_L.png", 0.1)]
ANIMATION_JUMP       = [("tiles/predator/jump_R.png", 0.1)]
ANIMATION_IDLE       = [("tiles/predator/idle_R-01.png"),
                        ("tiles/predator/idle_R-02.png"),
                        ("tiles/predator/idle_R-03.png"),
                        ("tiles/predator/idle_R-04.png"),
                        ("tiles/predator/idle_R-05.png"),
                        ("tiles/predator/idle_R-06.png")]

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
        self.image.set_colorkey(pygame.Color(COLOR))

        predatorAnim = []
        for anim in ANIMATION_RIGHT:
            predatorAnim.append((anim, ANIMATION_DELAY))
        self.predatorAnimRight = pyganim.PygAnimation(predatorAnim)
        self.predatorAnimRight.play()

        predatorAnim = []
        for anim in ANIMATION_LEFT:
            predatorAnim.append((anim, ANIMATION_DELAY))
        self.predatorAnimLeft = pyganim.PygAnimation(predatorAnim)
        self.predatorAnimLeft.play()

        predatorAnim = []
        for anim in ANIMATION_IDLE:
            predatorAnim.append((anim, ANIMATION_DELAY))
        self.predatorAnimIdle = pyganim.PygAnimation(predatorAnim)
        self.predatorAnimIdle.play()
        self.predatorAnimIdle.blit(self.image, (0, 0))

        self.predatorJumpRight = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.predatorJumpRight.play()

        self.predatorJumpLeft = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.predatorJumpLeft.play()

        self.predatorJump = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.predatorJump.play()

    def update(self, left, right, up, platforms):
        if left:
            self.xvel = -MOVE_SPEED
            self.image.fill(pygame.Color(COLOR))
            if up:
                self.predatorJumpLeft.blit(self.image, (0, 0))
            else:
                self.predatorAnimLeft.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED
            self.image.fill(pygame.Color(COLOR))
            if up:
                self.predatorJumpRight.blit(self.image, (0, 0))
            else:
                self.predatorAnimRight.blit(self.image, (0, 0))

        if not (left or right):
            self.xvel = 0
            if not up:
                self.image.fill(pygame.Color(COLOR))
                self.predatorAnimIdle.blit(self.image, (0, 0))

        if up:
            if self.on_ground:
                self.yvel = -JUMP_POWER
            self.image.fill(pygame.Color(COLOR))
            self.predatorJump.blit(self.image, (0, 0))    
        
        if not self.on_ground:
            self.yvel += GRAVITY

        self.on_ground = False

        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):

                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.on_ground = True
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0

