import pygame
from game.asset import Asset
import math
import numpy as np

class Bar(Asset):
    bar = None
    bar_pos = None
    MAX_SPEED = 200
    speed = 0
    last_pos = None
    new_pos = None
    previous_sample_time = 0
    bar_speed = 0.3

    def __init__(self, surface, screen, child_assets):
        super().__init__(surface, screen, child_assets)
        self.last_pos = pygame.Vector2(0,0)
        self.new_pos = pygame.Vector2(0, 0)

    def __distance(self, point1, point2):
        p1x, p1y = point1
        p2x, p2y = point2
        x_squared = (p2x - p1x) * (p2x - p1x)
        y_squared = (p2y - p1y) * (p2y - p1y)
        pixel_dist = math.sqrt(x_squared + y_squared)
        return pixel_dist

    def __x_direction(self, x_old, x_new):
        dir = 0
        diff = x_new - x_old
        if(diff != 0):
            dir = 1 if diff > 0 else -1
        return dir

    def load(self):
        self.bar = pygame.image.load("bar.png").convert_alpha()
        self.bar_pos = pygame.Vector2(self.surface.get_width() / 2 - self.bar.get_width() / 2,self.surface.get_height() - self.bar.get_height())

    def update(self, dt):

        #get mouse position
        self.new_pos = pygame.mouse.get_pos()
        ratio_x = (self.screen.get_width() / self.surface.get_width() )
        ratio_y = (self.screen.get_height() / self.surface.get_height())

        #we must scale the mouse position
        scaled_pos = (self.new_pos[0] / ratio_x, self.new_pos[1] / ratio_y)

        if self.new_pos[0] >= self.screen.get_width() - 1:
            pygame.mouse.set_pos(0, self.new_pos[1])
            self.last_pos = (0, scaled_pos[1])
            return
        elif self.new_pos[0] <= 0:
            pygame.mouse.set_pos(self.screen.get_width() - 1, self.new_pos[1])
            self.last_pos = (self.surface.get_width(), scaled_pos[1])
            return

        x_dir = 0
        pixels_movement = 0

        #if the new pos is different to the old pos, calculate movement displacement
        if self.new_pos != self.last_pos and dt != 0:
            pixels_movement = self.__distance(self.last_pos, scaled_pos)
            x_dir = self.__x_direction(self.last_pos[0], scaled_pos[0])
            self.last_pos = scaled_pos

        #calculate new position
        final_px_mov = x_dir * pixels_movement * self.bar_speed
        final_pos = self.bar_pos.x + final_px_mov

        # avoid the bar leaves the limits
        if final_pos > self.surface.get_width() - self.bar.get_width():
            self.bar_pos.x = self.surface.get_width() - self.bar.get_width()
        elif final_pos <= 0:
            self.bar_pos.x = 0
        else:
            self.bar_pos.x = final_pos

        for asset in self.child_assets:
            asset.update(dt)

    def draw(self, dt):
        self.surface.blit(self.bar, (self.bar_pos.x, self.bar_pos.y))
