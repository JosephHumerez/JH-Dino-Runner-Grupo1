import pygame

from random import randint
from components.obstacles.cactus import Cactus
from components.obstacles.bird import Bird
from utils.constants import LARGE_CACTUS, SMALL_CACTUS, BIRD, DEFAULT_TYPE,SHIELD_TYPE

class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self,game,dinosaur):
        if len(self.obstacles) == 0:
            self.obstacles.append(self.generate_obstacle())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if dinosaur.dino_rect.colliderect(obstacle.rect):
                if game.dinosaur.type == SHIELD_TYPE:
                    game.dinosaur.type = DEFAULT_TYPE
                    self.obstacles.pop()
                    game.powerup_manager.active = 0
                    game.powerup_manager.time = 0
                else:
                    pygame.time.delay(700)
                    game.playing = False

    
    def generate_obstacle(self):
        index_random = randint(0, 2)

        if index_random == 0:
            return Cactus(SMALL_CACTUS, 320)
        elif index_random == 1:
            return Cactus(LARGE_CACTUS, 295)
        elif index_random == 2:
            return Bird(BIRD, randint(80, 300))

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset(self):
        self.obstacles.clear()