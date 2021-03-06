import pygame as pg
import math
import conf


class Car(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.src_image = pg.image.load(conf.os.path.join(conf.img_folder, "blue_car.png")).convert_alpha()
        self.image = self.src_image
        self.image = pg.transform.scale(self.image, ((int(conf.WIDTH / 20)), int(conf.WIDTH / 20)))
        self.honk = pg.mixer.Sound(conf.os.path.join(conf.sound_folder, "honk.ogg"))
        self.rect = self.image.get_rect()
        self.rect.center = (conf.WIDTH / 2, conf.HEIGHT / 2)

        self.speed = self.direction = 0
        self.up = self.down = self.right = self.left = 0
        self.position = self.rect.center

        self.MAX_SPEED = 8
        self.MAX_BACKWARDS_SPEED = 5
        self.ACCELERATION_POS = 1.8
        self.ACCELERATION_NEG = 1.5
        self.TURN_SPEED = 5
        self.BREAK_SPEED = 0.75

    def update(self):
        key_press = pg.key.get_pressed()
        if key_press[pg.K_SPACE]:
            self.breaks()

        self.speed += (self.up + self.down)
        if self.speed > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        if self.speed < -self.MAX_BACKWARDS_SPEED:
            self.speed = -self.MAX_BACKWARDS_SPEED

        # calculating the direction and rotation
        self.direction += (self.right + self.left)

        x, y = self.position
        rad = self.direction * math.pi / 180

        # setting position according to speed and direction
        x += -self.speed * math.sin(rad)
        y += -self.speed * math.cos(rad)
        self.position = (x, y)

        self.image = pg.transform.rotate(self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    # function for the breaks of the car
    def breaks(self):
        temp = abs(self.speed) - self.BREAK_SPEED
        if temp <= 0:           # if the car is going to stop in next break set speed to 0
            self.speed = 0
        else:
            if self.speed > 0:
                self.speed -= self.BREAK_SPEED      # if the car is going forward
            else:
                self.speed += self.BREAK_SPEED      # if the car is going backwards

    def color_pick(self, color):
        if color == 'blue':
            self.src_image = pg.image.load(conf.os.path.join(conf.img_folder, "blue_car.png")).convert_alpha()
        if color == 'green':
            self.src_image = pg.image.load(conf.os.path.join(conf.img_folder, "green_car.png")).convert_alpha()
        if color == 'pink':
            self.src_image = pg.image.load(conf.os.path.join(conf.img_folder, "pink_car.png")).convert_alpha()
        if color == 'red':
            self.src_image = pg.image.load(conf.os.path.join(conf.img_folder, "red_car.png")).convert_alpha()
        self.image = self.src_image
        self.image = pg.transform.scale(self.image, ((int(conf.WIDTH / 20)), int(conf.WIDTH / 20)))
