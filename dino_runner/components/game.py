import pygame

from components.obstacles.obstacle_manager import ObstacleManager
from utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, GAME_OVER
from utils import text_utils

from components.dinosaur import Dinosaur
from components.powerups.powerup_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.games_played = 0
        self.game_running = True
        self.dinosaur = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.powerup_manager = PowerUpManager()

    def run(self):
        # Game loop: events - update - draw
        self.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()
            self.points +=  1
        
        self.games_played += 1
    
    def reset(self):
        self.obstacle_manager.reset()
        self.powerup_manager.reset()
        self.playing = True
        self.points = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.game_running = False

    def update(self):
        self.dinosaur.update(pygame.key.get_pressed())
        self.obstacle_manager.update(self, self.dinosaur)
        self.powerup_manager.update(self)

    def execute(self):
        while self.game_running:
            if not self.playing:
                self.show_menu()

    def show_menu(self):
        self.game_running = True

        white_color = (255, 255, 255)
        self.screen.fill(white_color)

        if self.games_played == 0:
            self.show_options_menu("Press any Key to Start")
        else:
            self.show_options_menu("Press any Key to Restart")
            self.show_score()

            self.screen.blit(GAME_OVER, (HALF_SCREEN_WIDTH -195, HALF_SCREEN_HEIGHT -100))

        pygame.display.update()

        self.handle_key_event_menu()

    def show_options_menu(self, text):
        text, text_rect = text_utils.get_text_element(text, HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT)

        self.screen.blit(text, text_rect)

    def handle_key_event_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.game_running = False
                pygame.display.quit()
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                self.run()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.show_score()
        self.dinosaur.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.powerup_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def show_score(self):
        if self.points % 100 == 0:
            self.game_speed += 1

        text, text_rect = text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    