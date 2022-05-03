import enum
from PondData import PondData
from Fish import Fish
# from run import Dashboard
from dashboard import Dashboard
from random import randint
from FishData import FishData

import random
import pygame
import pygame_menu
import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic, QtGui
import threading
from Client import Client

class Pond:

    def __init__(self):
        self.name = "sick-salmon"
        self.fishes = []
        self.moving_sprites = pygame.sprite.Group()
        self.sharkImage = pygame.image.load("./assets/images/sprites/shark.png")
        self.sharkImage = pygame.transform.scale(self.sharkImage, (128,128))
        self.msg = ""
        self.pondData = PondData(self.name)
        self.network = None
        self.sharkTime = 0
        self.displayShark = False

    def getPopulation(self):
        return len(self.fishes)
    
    def randomShark(self):
        dead = randint(0, len(self.fishes)-1)
        return self.fishes[dead]

    # def sharkAttack(self, screen, fish):
    #     screen.blit(self.sharkImage, (fish.getFishx(), fish.getFishy())) 
    #     self.removeFish(fish)
    #     fish.die()
           

    def spawnFish(self, parentFish = None):
        tempFish = Fish(100, 100, self.name, parentFish.getId())
        self.fishes.append(tempFish)
        self.moving_sprites.add(tempFish)
        
    def pheromoneCloud(self ):
        pheromone = randint(2, 20)
        for f in self.fishes:
            f.increasePheromone(pheromone)
        
            if f.isPregnant(): ## check that pheromone >= pheromone threshold
                newFish = Fish(50, randint(50, 650), self.name, f.getId())
                self.addFish( newFish)
                # self.pondData.addFish( newFish.fishData)
                
                f.resetPheromone()

    def migrateFish(self, fishIndex, destination):
        # destination = random.choice(self.network.other_ponds.keys())
        self.pondData.migrateFish(self.fishes[fishIndex].getId())
        self.network.migrate_fish(self.fishes[fishIndex].fishData, destination )
    #---------------implement---------------#

    def addFish(self, newFishData): #from another pond
        self.fishes.append(newFishData)
        self.pondData.addFish(newFishData.fishData)
        self.moving_sprites.add(newFishData)
        self.network.pondData = self.pondData

    
    def removeFish(self, fish):
        self.fishes.remove(fish)
        self.moving_sprites.remove(fish)

    def update(self, injectPheromone = False):
        for ind, f in enumerate( self.fishes): #checkout all the fish in the pond
            f.updateLifeTime() # decrease life time by 1 sec
            self.pondData.setFish(f.fishData)

            if f.getGenesis() != self.name and f.in_pond_sec >= 5:
                newFish = Fish(50, 50,f.fishData.genesis, f.fishData.id)
                self.addFish( newFish )
                # self.pondData.addFish( newFish.fishData )
            elif f.getGenesis() == self.name and f.in_pond_sec <= 15:
                if random.getrandbits(1):
                    dest = random.choice(self.network.other_ponds.keys())
                    self.migrateFish( ind, dest )
                    # self.network.migrate_fish(f, dest)
                    # self.pondData.migrateFish(f.getId())
                    parent = None
                    if f.parentId:
                        parent = f.parentId
                    for ind2, f2 in enumerate(self.fishes):
                        if parent and f2.fishData.parentId == parent or f2.fishData.parentId == f.id:
                            self.migrateFish( ind2, dest)
                            # self.network.migrate_fish( f2, dest)
                            # self.pondData.migrateFish(f2.getId())
                            break
                    continue
            else :
                dest = random.choice(self.network.other_ponds.keys())
                if self.getPopulation() > f.getCrowdThresh():
                    
                    self.migrateFish( ind, dest )
                    # self.network.migrate_fish(f, dest )
                    # self.pondData.migrateFish( f.fishData.id )
                continue
            
        if ( injectPheromone ):
            self.pheromoneCloud()
        # print("Client send :",self.pondData)
        self.network.pond = self.pondData

    def run(self):
        # General setup
        direction = 1
        speed_x = 3
        # speed_y = 4
        random.seed(123)
        
        self.network = Client(self.pondData)
        self.msg = self.network.get_msg()
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))

        bg = pygame.image.load("./assets/images/background/bg.jpg")
        bg = pygame.transform.scale(bg, (1280, 720))
        pygame.display.set_caption("Fish Haven Project")
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        pregnant_time = pygame.time.get_ticks()
        send_data_time = pygame.time.get_ticks()
        self.addFish(Fish(10,100))

        self.addFish(Fish(10,140, genesis="peem"))
        self.addFish(Fish(100,200, genesis="dang"))

        app = QApplication(sys.argv)

        running = True
        while running:

            if len(self.fishes) > 20:
                kill = randint(0, len(self.fishes) - 1)
                self.removeFish(self.fishes[kill])
                # self.fishes[kill].die()

            # print(self.network.get_msg())
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.network.disconnect()
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        print(self.fishes[0].getId())
                        d = Dashboard(self.fishes)
                        pond_handler = threading.Thread(target=app.exec_)
                        pond_handler.start()

            # print("POND:"+self.msg.__str__())
            # print("pond: ", self.pondData)
            self.msg = self.network.send_pond()
           # print(self.msg.data)
            if (self.msg.action == "MIGRATE"):
                newFish = Fish(50, 50, self.msg.data['fish'].genesis, self.msg.data['fish'].parentId)
                self.addFish(newFish)

                # self.pondData.addFish(newFish.fishData)
                self.network.pondData = self.pondData
                    
            screen.fill((0, 0, 0))
            screen.blit(bg,[0,0])

            
            for fish in self.moving_sprites:
                fish.move(speed_x)
                screen.blit(fish.image, fish.rect)
      
            
            time_since_enter = pygame.time.get_ticks() - start_time
            time_since_new_birth = pygame.time.get_ticks() - pregnant_time
            time_since_last_data_send = pygame.time.get_ticks() - send_data_time
            if (time_since_new_birth > 6000):
                self.pheromoneCloud()
                pregnant_time = pygame.time.get_ticks()

            #shark every 30 seconds
            if time_since_enter > 17500:
                deadFish = self.randomShark()
                screen.blit(self.sharkImage, (deadFish.getFishx()+30, deadFish.getFishy()))
                pygame.display.flip()
                pygame.event.pump()
                pygame.time.delay(500)
                self.removeFish(deadFish)
                deadFish.die()
                start_time = pygame.time.get_ticks()

            print(len(self.fishes))

            # if time_since_last_data_send > 2000:
            #     pass
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        