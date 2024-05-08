import pygame
from game.asset import Asset
import math as mt

class Ball(Asset):
    ball = None
    ball_pos = None
    ball_speed = None
    ball_speed_mod = 20
    ball_speed_angle = 45
    ball_id = -1

    def __init__(self, surface, screen, child_assets):
        super().__init__(surface, screen, child_assets)
        self.ball_pos = pygame.Vector2(1200,0)
        self.ball_speed = pygame.Vector2(1,5.2)

    def load(self):
        self.ball = pygame.image.load("ball.png").convert_alpha()

    def update(self, dt):
        vx = self.ball_speed_mod * mt.cos(mt.radians(self.ball_speed_angle))
        vy = self.ball_speed_mod * mt.sin(mt.radians(self.ball_speed_angle))
        #print(vx,vy)

        self.ball_pos.x += vx
        self.ball_pos.y += vy

        if self.ball_pos.x > self.surface.get_width() - self.ball.get_width():
            vx *= -1
            theta = mt.atan2(vy, vx)
            mirror_angle = mt.degrees(theta)
            self.ball_speed_angle = mirror_angle
        elif self.ball_pos.x <= 0:
            vx *= -1
            theta = mt.atan2(vy, vx)
            mirror_angle = mt.degrees(theta)
            self.ball_speed_angle = mirror_angle

        if self.ball_pos.y > self.surface.get_height() - self.ball.get_height():
            vy *= -1
            theta = mt.atan2(vy, vx)
            mirror_angle = mt.degrees(theta)
            self.ball_speed_angle = mirror_angle

        elif self.ball_pos.y <= 0:
            vy *= -1
            theta = mt.atan2(vy, vx)
            mirror_angle = mt.degrees(theta)
            self.ball_speed_angle = mirror_angle

        for asset in self.child_assets:
            asset.update(dt)

    def draw(self, dt):
        self.surface.blit(self.ball, (self.ball_pos.x, self.ball_pos.y))
        for asset in self.child_assets:
            asset.draw(dt)