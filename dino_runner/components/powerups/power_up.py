from random import randint
from pygame.sprite import Sprite
from utils.constants import SCREEN_WIDTH, HALF_SCREEN_WIDTH

class PowerUp(Sprite):

    def __init__(self, image, type):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = randint(HALF_SCREEN_WIDTH, SCREEN_WIDTH)
        self.rect.y = randint(80, 300)
        self.type = type
        self.time = 0
        self.active = False

    def update(self, game_speed, powerups):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            powerups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)