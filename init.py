import pygame
from game.game import Game

user_w = 640
user_h = 360
max_w = 1920
max_h = 1080
pygame.init()
screen = pygame.display.set_mode((user_w, user_h))
surface = pygame.Surface((max_w, max_h))
clock = pygame.time.Clock()
running = True
dt = 0
game = Game(surface, screen)
game.load()
pygame.display.set_caption("Breakout")
pygame.mouse.set_visible(0)
pygame.event.set_grab(True)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    game.update(dt)
    frame = game.draw(dt)
    screen.blit(frame, (0, 0))
    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()

import math

# Coordenadas del vector
x = 3.53
y = -3.53

# Calcula el ángulo con respecto al eje x
theta = math.atan2(y, x)

# Calcula el ángulo espejo con respecto al eje y
mirror_angle = math.pi - theta

# Imprime el resultado en radianes y grados
print("Ángulo espejo con respecto al eje y (radianes):", mirror_angle)
print("Ángulo espejo con respecto al eje y (grados):", math.degrees(mirror_angle))

if y < 0:
    mirror_angle = math.pi / 2 + theta
else:
    mirror_angle = 3 * math.pi / 2 + theta

print("Ángulo espejo con respecto al eje x (radianes):", mirror_angle)
print("Ángulo espejo con respecto al eje x (grados):", math.degrees(mirror_angle))