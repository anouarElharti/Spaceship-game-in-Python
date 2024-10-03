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
player_direction = pygame.math.Vector2()
player_speed = 300  # adjust this value to change the player speed

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
    delta_time = clock.tick() / 1000
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # moving the player using inputs
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     laser_rect.center = player_rec.center
        # if event.type == pygame.MOUSEMOTION:
        #     player_rec.center = event.pos

    # inputs for mooving the player
    keys = pygame.key.get_pressed()
    # moving the player using inputs
    player_direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
    player_direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

    #maintaining the speed in every direction
    if player_direction:
        player_direction = player_direction.normalize()
    else:
        player_direction = player_direction

    # capturing the fire strike
    recent_keys = pygame.key.get_just_pressed()
    if recent_keys[pygame.K_SPACE]:
        print("Strike")
    # applying the player direction
    player_rec.center += player_direction * player_speed * delta_time
    print((player_direction * player_speed).magnitude())

    # moving the player like DVD logo
    # player_rec.center += player_direction * player_speed * delta_time
    # if player_rec.bottom >= WINDOW_HEIGHT or player_rec.top <= 0:
    #     player_direction.y *= -1
    # if player_rec.right >= WINDOW_WIDTH or player_rec.left <= 0:
    #     player_direction.x *= -1
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