from PondData import PondData
from Fish import Fish
# from run import Dashboard
from dashboard import Dashboard
import random
import pygame
import pygame_menu
import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic, QtGui
import threading
from pond_sick_salmon import Client

class Pond:

    def __init__(self):
        self.name = "sick-salmon"
        self.fishes = []
        self.moving_sprites = pygame.sprite.Group()
        self.sharkImage = pygame.image.load("./assets/images/sprites/shark.png")
        self.sharkImage = pygame.transform.scale(self.sharkImage, (128,128))
        self.msg = ""
        self.pondData = PondData(self.name)

    def getPopulation(self):
        return len(self.fishes)
    
    def randomShark(self, screen):
        random.seed(123)
        
        attack = random.random()

        # if attack < 0.1:
        self.sharkAttack(screen, random.choice(self.fishes))
    
    def sharkAttack(self, screen, fish):
        screen.blit(self.sharkImage, (fish.getFishx(), fish.getFishy())) 
        self.removeFish(fish)
        fish.die()
           

    def spawnFish(self, parentFish = None):
        tempFish = Fish(100, 100, self.name, parentFish.getId())
        self.fishes.append(tempFish)
        self.moving_sprites.add(tempFish)
        
    def pheromoneCloud(self ):
        pheromone = random.randint(2, 20)
        for f in self.fishes:
            f.increasePheromone(pheromone)
            if f.isPregnant(): ## check that pheromone >= pheromone threshold
                self.fishes.append( Fish(10, 100, self.name, f.getId()))
                f.resetPheromone()

    def migrateFish(self, fishIndex):
        pass
    #---------------implement---------------#

    def addFish(self, newFishData): #from another pond
        self.fishes.append(newFishData)
        self.pondData.addFish(newFishData.fishData)
        self.moving_sprites.add(newFishData)
    
    def removeFish(self, fish):
        self.fishes.remove(fish)
        self.moving_sprites.remove(fish)

    def update(self, injectPheromone = False):
        for ind, f in enumerate( self.fishes): #checkout all the fish in the pond
            f.updateLifeTime() # decrease life time by 1 sec
            if f.getGenesis() != self.name and f.in_pond_sec >= 5:
                self.addFish( f )
            elif f.getGenesis() == self.name and f.in_pond_sec <= 15:
                if random.getrandbits(1):
                    self.migrateFish( ind ) 
                    continue
            
            if self.getPopulation() > f.getCrowdThresh():
                self.migrateFish( ind )
                continue
            
        if ( injectPheromone ):
            self.pheromoneCloud()

    def run(self):
        # General setup
        direction = 1
        speed_x = 3
        # speed_y = 4
        n = Client()
        self.msg = n.get_msg()
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))

        bg = pygame.image.load("./assets/images/background/bg.jpg")
        bg = pygame.transform.scale(bg, (1280, 720))
        pygame.display.set_caption("Fish Haven Project")
        clock = pygame.time.Clock()
        self.addFish(Fish(10,100))
        self.addFish(Fish(10,140, genesis="peem"))
        self.addFish(Fish(100,200, genesis="dang"))
        
        
        
        running = True
        while running:
            print(n.get_msg())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        print(self.fishes[0].getId())
                        app = QApplication(sys.argv)
                        d = Dashboard(self.fishes)
                        pond_handler = threading.Thread(target=app.exec_)
                        pond_handler.start()

            print("POND:"+self.msg.__str__())
            self.msg = n.send_pond(self.pondData)
                    
            screen.fill((0, 0, 0))
            screen.blit(bg,[0,0])

            
            for fish in self.moving_sprites:
                fish.move(speed_x)
                screen.blit(fish.image, fish.rect)
            
            # self.randomShark(screen)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        