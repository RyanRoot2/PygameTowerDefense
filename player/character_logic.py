import pygame

class CharacterLogic:
    def __init__(self, pos):
        self.health = 100
        self.mana = 50
        self._pos = pos
        self.direction = pygame.math.Vector2(0, 0)
        # other shared logic attributes

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, value):
        self._pos = value
        if hasattr(self, "sprite"):
            self.sprite.update_position(value)

    # Character movement logic
   
    def input(self):
        keys = pygame.key.get_pressed()
        input_vector = pygame.math.Vector2(0, 0)
        if keys[pygame.K_e]:
            input_vector.y -= 1
        if keys[pygame.K_d]:
            input_vector.y += 1
        if keys[pygame.K_s]:
            input_vector.x -= 1
        if keys[pygame.K_f]:
            input_vector.x += 1
        self.direction = input_vector
    
    def move(self):
        speed = 2  # pixels per second
        self.pos += self.direction * speed
    
    def update(self):
        self.input()
        self.move()
        # other update logic