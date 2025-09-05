"""Provides a centralized way to retrieve assets.

Assets are loaded using the importlib.resources module to ensure compatibility
with various packaging methods.

Each asset type (images, sounds, fonts, levels, UI elements) is represented by an Enum.
Each Enum member has a method to load the asset.
Enums were chosen to avoid hardcoding strings throughout the codebase.

Usage:
    from tower_defense.utils.asset_manager import Images
    image = Images.CONSECRATION.load()  # Returns pygame surface.
"""

from enum import Enum, unique
from functools import cache
from importlib.resources import as_file, files
from pathlib import Path

import pygame as pg

ASSETS_PATH = files("tower_defense.assets")
IMAGES_PATH = ASSETS_PATH / "images"
SOUNDS_PATH = ASSETS_PATH / "sounds"
FONTS_PATH = ASSETS_PATH / "fonts"
LEVELS_PATH = ASSETS_PATH / "levels"
UI_PATH = ASSETS_PATH / "ui"


@unique
class Images(Enum):
    CONSECRATION = "consecration.png"
    PALADIN = "paladin.png"
    TOWER = "tower.png"
    ZOMBIE = "zombie.png"

    @cache
    def load(self) -> pg.Surface:
        with as_file(IMAGES_PATH / self.value) as path:
            assert path.is_file(), f"Image file not found: {path}"
            return pg.image.load(path).convert_alpha()


@unique
class Sounds(Enum):
    # Web builds with PygBag only support OGG sounds.
    EXPLOSION = "explosion.wav"
    SHOOT = "shoot.wav"
    BACKGROUND_MUSIC = "background.mp3"

    @cache
    def load(self) -> pg.Sound:
        # TODO: Music should probably be its own Enum that loads with pg.mixer.music.
        with as_file(SOUNDS_PATH / self.value) as path:
            assert path.is_file(), f"Sound file not found: {path}"
            return pg.Sound(path)


@unique
class Fonts(Enum):
    ARIAL = "arial.ttf"
    COMIC_SANS = "comic_sans.ttf"

    @cache
    def load(self) -> pg.Font:
        with as_file(FONTS_PATH / self.value) as path:
            assert path.is_file(), f"Font file not found: {path}"
            # Default point size is 20; can be changed later.
            return pg.font.Font(path)


@unique
class Levels(Enum):
    LEVEL_1 = "level_1.json"
    LEVEL_2 = "level_2.json"

    @cache
    def load(self) -> Path:
        with as_file(LEVELS_PATH / self.value) as path:
            assert path.is_file(), f"Level file not found: {path}"
            return path


@unique
class UIElements(Enum):
    BUTTON = "button.png"
    PANEL = "panel.png"

    @cache
    def load(self):
        with as_file(IMAGES_PATH / self.value) as path:
            assert path.is_file(), f"Image file not found: {path}"
            return pg.image.load(path).convert_alpha()
