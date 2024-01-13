import pygame
import spritesheet

pygame.init()

# screen config
H = 500
W = 500
mid_h = H // 2
mid_w = W // 2
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Link sprite-sheets")

# colors
BG = (50, 50, 50)
BLACK = (0, 0, 0)
SPRITE_BG = (146, 144, 255)

running = True
while running:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update screen
    screen.fill(BG)

    # update animation
    current_time = pygame.time.get_ticks()
    pygame.display.update()
pygame.quit()