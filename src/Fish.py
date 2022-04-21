import pygame
import sys
from src.FishData import FishData

class Fish(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, parent = None):
        super().__init__()
        self.attack_animation = False
        self.sprites = []
        self.loadSprite("./assets/images/sprites/")
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.fishData = FishData(parent)

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

    def increasePheromone(self, n):
        self.fishData.pheromone += n
        if self.fishData.pheromone > self.fishData.pheromoneThresh:
            self.giveBirth()

    def giveBirth(self):
        self.fishData.genesis.spawnFish(self)

    def migrate(self):
        pass
    
    def getId(self):
        return self.fishData.id

    def isPregnant(self):
        return self.fishData.pheromone >= self.fishData.pheromoneThresh

    def updateLifeTime(self):
        self.fishData.lifetime -= 1

