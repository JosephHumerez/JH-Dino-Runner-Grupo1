import pygame
from components.obstacles.cactus import Cactus
from utils.constants import LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self,game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.dinosaur.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False 

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)