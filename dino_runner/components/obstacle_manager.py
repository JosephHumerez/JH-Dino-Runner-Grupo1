from components.cactus import Cactus
from utils.constants import LARGE_CACTUS, SMALL_CACTUS

from components.bird import Bird
from utils.constants import BIRD


class ObstacleManager():
    def __init__(self):
        self.obstacles = []

    def update(self):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(SMALL_CACTUS))
            self.obstacles.append(Cactus(LARGE_CACTUS))

            self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(15, self.obstacles)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)