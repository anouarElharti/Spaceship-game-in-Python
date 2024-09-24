import pygame
from os.path import join
from random import randint

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 680
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

running = True

# create a plain surface
surf = pygame.Surface((100, 200))
x, y = 100, 150
surf.fill("red")

# importing image
player_surface = pygame.image.load(join("images", "player.png")).convert_alpha()
stars_surface = pygame.image.load(join("images", "star.png")).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # drawing the game
    display_surface.fill("darkgray")
    # positioning the stars between the background surface and the player surface
    for position in star_positions:
        display_surface.blit(stars_surface, position)
    # add the surf to the display
    # x += .1 # animating the surface by adding to the x value
    display_surface.blit(player_surface, (x, y))
    pygame.display.update()

pygame.quit()