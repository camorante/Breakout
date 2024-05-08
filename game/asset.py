from abc import ABCMeta, abstractmethod
class Asset(metaclass=ABCMeta):
    surface = None
    screen = None
    child_assets = []

    def __init__(self, surface, screen, child_assets=None):
        if child_assets is None:
            child_assets = []
        self.surface = surface
        self.screen = screen
        self.child_assets = child_assets

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def draw(self, dt):
        pass