import pygame
import sys
import random

from FishData import FishData

class Fish(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, genesis="sick-salmon", parent = None):
        super().__init__()
        self.fishData = FishData(genesis, parent)
         
        #swimming controller
        self.direction = "RIGHT"
        self.face = 1
        self.attack_animation = False
        self.sprites = [] #Main sprite
        self.leftSprite = []
        self.rightSprite = []
        self.loadSprite(genesis)

        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.rect.left = pos_x
        self.rect.top = pos_y
        self.rect.right = pos_x + 100
        self.attack_animation = True
        self.current_sprite = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        self.in_pond_sec = 0

    def getFishData(self):
        return self.fishData

    def getFishTLPos(self):
        return self.rect.topleft
    
    def getFishx(self):
        return self.rect.left

    def getFishy(self):
        return self.rect.top

    def die(self):
        self.kill()


    def flipSprite(self):

        if self.face == 1:
            self.sprites=self.rightSprite
        elif self.face == -1:
            self.sprites=self.leftSprite
            
        self.current_sprite = 0

    def loadSprite(self, genesis):
        path = "./assets/images/sprites/"
        if genesis == "sick-salmon":
            path += "local-pond/"
        else:
            path += "foreign-pond/"

        self.loadSpriteRight(path, self.sprites)
        self.loadSpriteLeft(path)
        self.loadSpriteRight(path, self.rightSprite)

    def loadSpriteRight(self, path, spriteContainer):
        for i in range(1, 5):
            fish_path = path + str(i) + ".png"
            img = pygame.image.load(str(fish_path))
            img = pygame.transform.scale(img, (100, 100))
            img = pygame.transform.flip(img, True, False)
            spriteContainer.append(img)
        self.current_sprite = 0
        

    def loadSpriteLeft(self, path):
        for i in range(1, 5):
            fish_path = path + str(i) + ".png"
            img = pygame.image.load(fish_path)
            img = pygame.transform.scale(img, (100, 100))
            self.leftSprite.append(img)
        self.current_sprite = 0
    
    def update(self, speed):
        if self.attack_animation == True:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]
  

    def move(self, speed_x):
        if self.rect.left <= 0:
            print("chon left")
            self.face = 1
            print("x axis" + str(self.rect.left) + str(self.face))
            self.flipSprite()
        
        elif self.rect.left >= 1180:
            print("chon right")
            self.face = -1
            print("x axis" + str(self.rect.left)  + str(self.face))
            self.flipSprite()

        speed_x = random.randint(1, 5) * self.face

        self.rect.x += speed_x
        self.update(0.05)

    def increasePheromone(self, n):
        self.fishData.pheromone += n

    def migrate(self):
        pass
    
    def getId(self):
        return self.fishData.id

    def isPregnant(self):
        return self.fishData.pheromone >= self.fishData.pheromoneThresh

    def updateLifeTime(self):
        self.in_pond_sec += 1
        self.fishData.lifetime -= 1
        if self.fishData.lifetime == 0:
            self.fishData.status = "dead"

    def resetPheromone(self):
        self.fishData.pheromone = 0
    
    def getGenesis(self):
        return self.fishData.genesis

