import pygame
import spritesheet

pygame.init()

# screen config
H = 500
W = 500
mid_h = H // 2
mid_w = W // 2
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Mario spritesheets")

# colors
BG = (50, 50, 50)
BLACK = (0, 0, 0)
SPRITE_BG = (146, 144, 255)

# sprites
sprite_sheet_img = pygame.image.load("mario_spritesheet.png").convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_img)
size = 16

# animation
animation_list = []
animation_steps = [4, 1]
action = 0
last_update = pygame.time.get_ticks()
animation_cooldown = 100
frame = 0
step_counter = 0

for animation in animation_steps:
    temp_img_list = []
    for _ in range(animation):
        temp_img_list.append(sprite_sheet.get_image(step_counter, size, size, 4, SPRITE_BG))
        step_counter += 1
    animation_list.append(temp_img_list)


running = True
while running:
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and action > 0:
                action -= 1
                frame = 0
            if event.key == pygame.K_UP and action < len(animation_list) - 1:
                action += 1
                frame = 0

    # update screen
    screen.fill(BG)

    # update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list[action]):
            frame = 0

    # show frame image
    screen.blit(animation_list[action][frame], (mid_w - size*2, mid_h - size*2))

    pygame.display.update()
pygame.quit()
