import pygame


class HealthBar:
    def __init__(
        self,
        width: int,
        height: int,
        color: pygame.Color,
        attached_object=None,
        border=False,
        pos: tuple[int, int] | None = None,
    ):
        self.width = width
        self.height = height
        self.color = color
        self.attached_object = attached_object
        self.border = border
        # I don't understand why pos defaults to None. Setting to (0, 0) for typing.
        self.pos = pos or (0, 0)

    def determine_position(self):
        if self.attached_object and hasattr(self.attached_object, "sprite"):
            x, y = self.attached_object.sprite.rect.topleft
            self.pos = (x, y - 20)
        elif not self.pos:
            raise ValueError("HealthBar requires either an attached_object with a sprite or a fixed pos.")

    def draw(self, surface: pygame.Surface, health, max_health):
        health_ratio = health / max_health
        remaining_health_width = self.width * health_ratio
        self.determine_position()
        bg_rect = (self.pos[0], self.pos[1], self.width, self.height)

        if self.border:
            fg_rect = (self.pos[0] + 2, self.pos[1] + 2, remaining_health_width - 4, self.height - 4)
        else:
            fg_rect = (self.pos[0], self.pos[1], remaining_health_width, self.height)

        pygame.draw.rect(surface, (0, 0, 0), bg_rect)
        pygame.draw.rect(surface, self.color, fg_rect)
