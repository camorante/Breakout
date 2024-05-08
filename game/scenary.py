from game.asset import Asset
import pygame

class Scenary(Asset):
    back = None
    def __init__(self, surface, screen, child_assets):
        super().__init__(surface, screen, child_assets)

    def load(self):
        for asset in self.child_assets:
            asset.load()
        self.back = pygame.image.load("background.png").convert_alpha()

    def update(self, dt):
        for asset in self.child_assets:
            asset.update(dt)

    def draw(self, dt):
        self.surface.blit(self.back, (0, 0))
        for asset in self.child_assets:
            asset.draw(dt)

