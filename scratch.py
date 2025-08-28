# character_sprite.py
# manages loading and displaying sprites
class SpriteManager(pygame.sprite.Sprite):

# character_logic.py
# character logic that is shared, e.g. movement
class CharacterLogic:
    def __init__(self, pos, image):
        self.sprite = SpriteManager(..., pos, image)


# knight.py
# Character class, Knight, Mage, Warrior, etc.
# Each in their own file, inheriting from CharacterLogic
# Contains unique abilities and stats
from character_logic import CharacterLogic
class Knight(CharacterLogic):
    def __init__(self, pos):
        super().__init__(pos)
        self.honour = 50
        self.image = pygame.image.load(...).convert()
        # unique knight logic

# factory.py
# "Factory" or "Manager" class to handle creation of character-class objects
from knight import Knight
from mage import Mage
class CharacterFactory:
    @staticmethod
    def create(character_type, pos):
        if character_type == "knight":
            return Knight(pos)
        elif character_type == "mage":
            return Mage(pos)
