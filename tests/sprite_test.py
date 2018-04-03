import pygame
import os

pygame.init()

WIDTH = 800
HEIGHT = 600
SPRITES_PATH = '../assets/'

# import all the sprites
SPRITES = [SPRITES_PATH + f for f in os.listdir(SPRITES_PATH) if os.path.isfile(os.path.join(SPRITES_PATH , f))]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sprite test')
clock = pygame.time.Clock()


# main game loop
def game_loop():
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        window.fill(WHITE)

        # image test
        x = 0
        for i in SPRITES:
            img = pygame.image.load(i)
            (h, w) = img.get_rect().size
            window.blit(img, (x, 0))
            x += h + 10

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()
