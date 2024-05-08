import pygame

from game.ball import Ball
from game.bar import Bar
from game.scenary import Scenary
class Game:
    user_w = 1280
    user_h = 720
    max_w = 1920
    max_h = 1080
    dt = 0
    ball = None
    player_pos = pygame.Vector2(0,0)
    surface = None
    screen = None
    bar = None
    scenary = None
    ball = None

    def __init__(self, surface, screen):
        self.surface = surface
        self.screen = screen

        self.user_w = screen.get_width()
        self.user_h = screen.get_height()
        self.max_w = surface.get_width()
        self.max_h = surface.get_height()

        self.player_pos = pygame.Vector2(self.surface.get_width() / 2, self.surface.get_height() / 2)
        self.bar = Bar(surface, screen,[])
        self.ball = Ball(surface, screen,[])
        self.scenary = Scenary(surface, screen,[self.bar, self.ball])

    def load(self):
        #self.ball = pygame.image.load("ball.png").convert_alpha()
        self.scenary.load()

    def update(self, dt):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player_pos.y -= 1500 * dt
        if keys[pygame.K_s]:
            self.player_pos.y += 1500 * dt
        if keys[pygame.K_a]:
            self.player_pos.x -= 1500 * dt
        if keys[pygame.K_d]:
            self.player_pos.x += 1500 * dt
        self.scenary.update(dt)

    def draw(self, dt):
        self.surface.fill("white")
        self.scenary.draw(dt)
        #self.bar.draw(dt)
        #self.surface.blit(self.ball, (self.player_pos.x - self.ball.get_width() / 2, self.player_pos.y - self.ball.get_height() / 2))
        frame = pygame.transform.scale(self.surface, (self.user_w / self.max_w * self.max_w, self.user_h / self.max_h * self.max_h))
        return frame
