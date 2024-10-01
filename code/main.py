import pygame
from os.path import join
from random import randint

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 650
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")

running = True
clock = pygame.time.Clock()

# importing image
player_surface = pygame.image.load(join("images", "player.png")).convert_alpha()
player_rec = player_surface.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
player_direction = pygame.math.Vector2(1, 1)
player_speed = 200  # adjust this value to change the player speed

# importing the stars
stars_surface = pygame.image.load(join("images", "star.png")).convert_alpha()
star_positions = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

# importing meteor
meteor_surface = pygame.image.load(join("images", "meteor.png")).convert_alpha()
meteor_rec = meteor_surface.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# importing the laser
laser_surface = pygame.image.load(join("images", "laser.png")).convert_alpha()
laser_rect = laser_surface.get_rect(bottomleft = (20, WINDOW_HEIGHT - 20))

while running:
    delta_time = clock.tick(10) / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # moving the player
    player_rec.center += player_direction * player_speed * delta_time
    if player_rec.bottom > WINDOW_HEIGHT or player_rec.top < 0:
        player_direction.y *= -1
    if player_rec.right > WINDOW_WIDTH or player_rec.left < 0:
        player_direction.x *= -1
    # drawing the game
    display_surface.fill("darkgray")
    # drawing the stars
    for position in star_positions:
        display_surface.blit(stars_surface, position)
    # drawing the meteor
    display_surface.blit(meteor_surface, meteor_rec)
    # drawing the laser
    display_surface.blit(laser_surface, laser_rect)

    # drawing the player
    display_surface.blit(player_surface, player_rec)

    # updating the display
    pygame.display.update()


pygame.quit()