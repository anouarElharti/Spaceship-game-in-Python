import pygame

# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

running = True

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # drawing the game

pygame.quit()