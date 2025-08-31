import pygame

class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, pos, image_path, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

    def update_position(self, new_pos):
        self.rect.topleft = new_pos
