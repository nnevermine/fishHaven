import pygame
import sys
import random
from .Fish import Fish

class Pond:
    def __init__(self):
        self.pondName = "Sick Salmon"
        self.fishList = []
        self.moving_sprites = pygame.sprite.Group()

    def addFish(self, fish):
        self.fishList.append(fish)
        self.moving_sprites.add(fish)
    

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
        self.addFish(Fish(100,100))
        
        
        running = True
        while running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill((0, 0, 0))
            screen.blit(bg,[0,0])
            self.moving_sprites.draw(screen)
            
            
            for fish in self.moving_sprites:
                if fish.rect.left <= 0 or fish.rect.left >= 1180:
                    direction *= -1
                    speed_x = random.randint(0, 4) * direction
                    # speed_y = random.randint(0, 5) * direction
                    fish.flipSprite()
                    
                    if speed_x == 0:
                        speed_x = random.randint(2, 4) * direction


                        # speed_y = random.randint(2, 5) * direction
            
                # if fish.rect.top <= 40 or fish.rect.top >= 620:
                #     direction *= -1
                #     speed_x = random.randint(0, 5) * direction
                #     speed_y = random.randint(0, 5) * direction
        
                #     if speed_x == 0 and speed_y == 0:
                #         speed_x = random.randint(2, 5) * direction
                #         speed_y = random.randint(2, 5) * direction
                    
                fish.move(speed_x)
                fish.update(0.15)
                screen.blit(fish.image, fish.rect)
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()