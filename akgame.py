import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = pygame.Rect((300, 250, 50, 50))

pygame.display.set_caption("akgame V1.0.0")

run = True
while run:

    location = screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (0, 127, 255), player)

    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
        #holding keypress 'r' removes player
        invisible = pygame.key.get_pressed()
    if key[pygame.K_r] == True:
        location = screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
