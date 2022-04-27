from src.Fish import Fish
import random
import pygame
import sys

class Pond:
    # def __init__(self):
#         self.pondName = "Sick Salmon"
#         self.status = "alive"
#         self.fishList = []
#         self.population = len(self.fishList)
#         self.moving_sprites = pygame.sprite.Group()
#         self.all_moving_sprites=[]

    def __init__(self):
        self.name = "sick-salmon"
        self.fishes = []
        self.moving_sprites = pygame.sprite.Group()

    def getPopulation(self):
        return len(self.fishes)

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
        self.moving_sprites.add(newFishData)

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

        pygame.init()
        screen = pygame.display.set_mode((1280, 720))

        bg = pygame.image.load("./assets/images/background/bg.jpg")
        bg = pygame.transform.scale(bg, (1280, 720))
        pygame.display.set_caption("Fish Haven Project")
        clock = pygame.time.Clock()
        self.addFish(Fish(10,100))
        
        
        running = True
        while running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 0, 0))
            screen.blit(bg,[0,0])
            # self.moving_sprites.draw(screen)
            # print(self.moving_sprites)
            
            for fish in self.moving_sprites:
                fish.move(speed_x)
                screen.blit(fish.image, fish.rect)
                
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
        
# import pygame
# import sys
# import random
# from .Fish import Fish

# class Pond:
#     def __init__(self):
#         self.pondName = "Sick Salmon"
#         self.status = "alive"
#         self.fishList = []
#         self.population = len(self.fishList)
#         self.moving_sprites = pygame.sprite.Group()
#         self.all_moving_sprites=[]

#     def addFish(self, fish):
#         self.fishList.append(fish)
#         self.moving_sprites.add(fish)
    

#     def run(self):
#         # General setup
#         direction = 1
#         speed_x = 3
#         # speed_y = 4

#         pygame.init()
#         screen = pygame.display.set_mode((1280, 720))

#         bg = pygame.image.load("./assets/images/background/bg.jpg")
#         bg = pygame.transform.scale(bg, (1280, 720))
#         pygame.display.set_caption("Fish Haven Project")
#         clock = pygame.time.Clock()
#         self.addFish(Fish(100,100))
#         self.addFish(Fish(200,200))
        
        
#         running = True
#         while running:
            
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#             screen.fill((0, 0, 0))
#             screen.blit(bg,[0,0])
#             # self.moving_sprites.draw(screen)
#             # print(self.moving_sprites)
            
#             for fish in self.moving_sprites:
#                 fish.move(speed_x)

#                 # if fish.rect.left <= 0 or fish.rect.left >= 1180:
#                 #     direction *= -1
#                 #     speed_x = random.randint(0, 4) * direction
#                 #     # speed_y = random.randint(0, 5) * direction
#                 #     fish.flipSprite()
                    
#                 #     if speed_x == 0:
#                 #         speed_x = random.randint(2, 4) * direction
                    
#                 # fish.update(0.15)
#                 screen.blit(fish.image, fish.rect)
#             pygame.display.flip()
#             clock.tick(60)

#         pygame.quit()