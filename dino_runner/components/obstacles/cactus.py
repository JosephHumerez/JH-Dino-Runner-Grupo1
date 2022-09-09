import random
from components.obstacles.obstacle import Obstacle

class Cactus(Obstacle):
    def __init__(self, image, y):
        self.index = random.randint(0,2)
        super().__init__(image, random.randint(0,2))
        self.rect.y = y
