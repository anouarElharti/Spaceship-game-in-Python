import pygame
from os.path import join
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "player.png")).convert_alpha()
        self.rect = self.image.get_rect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.direction = pygame.math.Vector2()
        self.speed = 300
        self.space_pressed = False

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        if self.direction:
            self.direction = self.direction.normalize()
        else:
            self.direction = self.direction

        self.rect.center += self.direction * self.speed * delta_time
        


pygame.init()


# general setup
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 650
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Invaders")


running = True
clock = pygame.time.Clock()


# sprite groups
all_sprites = pygame.sprite.Group()
player = Player(all_sprites)


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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not player.space_pressed:
                print("Strike")
                player.space_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.space_pressed = False


    all_sprites.update(delta_time)


    # drawing the game
    display_surface.fill("darkgray")
    # drawing the stars
    for position in star_positions:
        display_surface.blit(stars_surface, position)
    # drawing the meteor
    display_surface.blit(meteor_surface, meteor_rec)
    # drawing the laser
    display_surface.blit(laser_surface, laser_rect)
    # drawing all the sprites
    all_sprites.draw(display_surface)
    # updating the display
    pygame.display.update()



pygame.quit()