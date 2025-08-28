import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Pygame Window")


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("assets/paladin.png").convert()
        self.rect = self.image.get_rect(topleft=pos)

player = Player((100, 100))
all_sprites = pygame.sprite.Group(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # Fill the screen with black
    all_sprites.draw(screen)
    


      # Fill the screen with black
    pygame.display.flip()  # Update the display