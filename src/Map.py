import pygame as pg
import conf


class Map(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(conf.os.path.join(conf.img_folder, "map.png"))
        self.image = pg.transform.scale(self.image, (conf.WIDTH, conf.HEIGHT))
        self.rect = self.image.get_rect()

        self.BORDER_TOP = conf.HEIGHT / 10
        self.BORDER_BOTTOM = conf.HEIGHT - self.BORDER_TOP
        self.BORDER_LEFT = conf.WIDTH / 15
        self.BORDER_RIGHT = conf.WIDTH - self.BORDER_LEFT
        self.BORDER = (self.BORDER_TOP, self.BORDER_BOTTOM, self.BORDER_LEFT, self.BORDER_RIGHT)