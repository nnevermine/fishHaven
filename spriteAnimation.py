
   
import pygame
import sys
import random

# from src.Fish import Fish
from src.Pond import Pond

pond = Pond()
pond.run()



# import pygame
# import sys

# from src.Fish import Fish
# from src.Pond import Pond
# # General setup
# pygame.init()
# clock = pygame.time.Clock()
# screen_width = 1280
# screen_height = 720

# bg = pygame.image.load("./assets/images/background/bg.jpg")
# bg = pygame.transform.scale(bg, (screen_width, screen_height)) 

# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Sprite Animation")
# # screen.fill((0,0,0))
# # screen.blit(bg,[0,0])
# # pygame.display.flip()

# # running = True

# # while running:
# #   for event in pygame.event.get():
# #     if event.type == pygame.QUIT:
# #       running = False

# # # Creating the sprites and groups
# moving_sprites = pygame.sprite.Group()
# fish = Fish(10, 100)
# moving_sprites.add(fish)
# start_ticks = None
# pond = Pond

# while True:
#     if start_ticks == None:
#         start_ticks = pygame.time.get_ticks()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.KEYDOWN:
#             fish.attack()
#     seconds = (pygame.time.get_ticks() - start_ticks) / 1000
#     if (seconds >= 1):
#         pond.update()
#         start_ticks = None

#     # Drawing
#     screen.fill((0, 90, 90))
#     screen.blit(bg,[0,0])
#     moving_sprites.draw(screen)
#     moving_sprites.update(0.05)
#     pygame.display.flip()
#     clock.tick(60)



# class Player(pygame.sprite.Sprite):
#     def __init__(self, pos_x, pos_y):
#         super().__init__()
#         self.attack_animation = False
#         self.sprites = []
#         self.sprites.append(pygame.image.load('fish1.png'))
#         self.sprites.append(pygame.image.load('fish2.png'))
#         self.sprites.append(pygame.image.load('fish3.png'))
#         self.sprites.append(pygame.image.load('fish4.png'))
#         self.sprites.append(pygame.image.load('fish5.png'))
#         self.sprites.append(pygame.image.load('fish6.png'))
#         self.sprites.append(pygame.image.load('fish7.png'))
#         self.current_sprite = 0
#         self.image = self.sprites[self.current_sprite]

#         self.rect = self.image.get_rect()
#         self.rect.topleft = [pos_x, pos_y]

#     def attack(self):
#         self.attack_animation = True

#     def update(self, speed):
#         if self.attack_animation == True:
#             self.current_sprite += speed
#             if int(self.current_sprite) >= len(self.sprites):
#                 self.current_sprite = 0
#                 # self.attack_animation = False

#         self.image = self.sprites[int(self.current_sprite)]


# # General setup
# pygame.init()
# clock = pygame.time.Clock()

# # Game Screen
# screen_width = 800
# screen_height = 800
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Sprite Animation")

# # Creating the sprites and groups
# moving_sprites = pygame.sprite.Group()
# player = Player(10, 100)
# moving_sprites.add(player)


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         if event.type == pygame.KEYDOWN:
#             player.attack()

#     # Drawing
#     screen.fill((0, 90, 90))
#     moving_sprites.draw(screen)
#     moving_sprites.update(0.05)
#     pygame.display.flip()
#     clock.tick(60)

