import pygame as pg
import conf
import random as rand


class ParkSpace(pg.sprite.Sprite):
    def __init__(self, bg_border):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(conf.os.path.join(conf.img_folder, "park_space.png"))
        self.rect = self.image.get_rect()
        (self.w, self.h) = self.rect.size

        # direction of the parking space
        left = rand.randint(0, 1)
        if left:
            self.image = pg.transform.rotate(self.image, 180)

        # see if the parking space is going to be by top or bottom edge
        BORDER_TOP = bg_border[0]
        BORDER_BOTTOM = bg_border[1]
        BORDER_LEFT = bg_border[2]
        BORDER_RIGHT = bg_border[3]

        offset = int(conf.WIDTH / 1.5)
        random_offset = rand.randint(0, offset)
        if rand.randint(0, 1):
            if left:        # top left
                self.rect.center = (BORDER_LEFT + (self.w / 2) + random_offset, BORDER_TOP + (self.h / 2))
            else:           # top right
                self.rect.center = (BORDER_RIGHT - (self.w / 2) - random_offset, BORDER_TOP + (self.h / 2))
        else:
            if left:        # bottom left
                self.rect.center = (BORDER_LEFT + (self.w / 2) + conf.WIDTH / 4 + random_offset / 2, BORDER_BOTTOM - (self.h / 2))
            else:           # bottom right
                self.rect.center = (BORDER_RIGHT - (self.w / 2) - random_offset, BORDER_BOTTOM - (self.h / 2))

    def parked(self, car):
        align_ver = car.rect.top >= self.rect.top and car.rect.bottom <= self.rect.bottom
        align_hor = car.rect.left >= self.rect.left and car.rect.right <= self.rect.right
        if align_ver and align_hor:
            per_ver = abs(self.rect.center[0] - car.rect.center[0])
            per_hor = abs(self.rect.center[1] - car.rect.center[1])
            per = 25 - (per_ver + per_hor)
            return per / 25
        else:
            return 0
