
   
# import pygame
# import sys
# import random

# # from src.Fish import Fish
# from src.Pond import Pond

# pond = Pond()
# pond.run()

import pygame

class Dashboard:
    def __init__(self, allFish=None):
        self.allFish = allFish
        print(self.allFish[0].getId())


    def run(self):
        
        clock = pygame.time.Clock()
        background_colour = (255,255,255)
        (width, height) = (1280, 710)
        screen = pygame.display.set_mode((width, height))

        pygame.display.set_caption('Dashboard')
        screen.fill(background_colour)


        pygame.display.flip()
        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            

            screen.fill((255,255,255))

            pygame.display.flip()

            clock.tick(30)

