import pygame
import sys

class Fish(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.attack_animation = False
        self.sprites = []
        self.loadSprite("./assets/images/sprites/")
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

    def loadSprite(self, path):
        for i in range(1, 6):
            fish_path = path + str(i) + ".png"
            self.sprites.append(pygame.image.load(fish_path))
        self.current_sprite = 0

    def attack(self):
        self.attack_animation = True

    def update(self, speed):
        if self.attack_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                # self.attack_animation = False

        self.image = self.sprites[int(self.current_sprite)]

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y
