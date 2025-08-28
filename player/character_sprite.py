import pygame

class CharacterSprite(pygame.sprite.Sprite):
    def __init__(self, pos, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

    def update_position(self, new_pos):
        self.rect.topleft = new_pos
