from random import randint
import pygame
from components.powerups.shield import Shield
from utils.constants import DEFAULT_TYPE



class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.time = 0
        self.active = False

    def update(self, game):
        if len(self.power_ups) == 0 and game.dinosaur.type == DEFAULT_TYPE:
            self.power_ups.append(self.generate_power_up())

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)

            if game.dinosaur.dino_rect.colliderect(power_up.rect):
                game.dinosaur.type = power_up.type
                self.active = True

        if self.time > 75:
            game.dinosaur.type = DEFAULT_TYPE
            self.active = False
            self.time = 0

        if self.active:
            self.time += 1

    def generate_power_up(self):
        return Shield()

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups.clear()