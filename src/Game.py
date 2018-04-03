import pygame as pg
import conf
import src.Car as Car


class Game:
    def __init__(self):
        pg.init()  # initialization of pg module
        pg.mixer.init()  # initialization of mixer used for sounds in a game
        self.screen = pg.display.set_mode((conf.WIDTH, conf.HEIGHT))  # setup a display
        pg.display.set_caption(conf.CAPTION)  # screen title
        self.clock = pg.time.Clock()  # game clock
        self.change = 0
        self.sprites = pg.sprite.Group()    # initialise group of sprites

        self._done = False
        self.init()

    # initalization of game object
    def init(self):
        global car
        car = Car.Car() # TODO : this is stupid
        self.sprites.add(car)  # add car to sprites

    def game_loop(self):
        while not self._done:

            self.clock.tick(conf.FPS)  # FPS argument of tick() is how many frames per second we want
            # EVENT LOGIC : event - handling loop
            for event in pg.event.get():  # go through list of events per second
                if event.type == pg.QUIT:  # look if user closed the window
                    self._done = True  # TODO: change the way you exit game loop

                down = event.type == pg.KEYDOWN
                if down:
                    if event.key == pg.K_RIGHT and abs(car.speed) > 1.25:       # car cannot turn with a small speed
                        car.right = down * -car.TURN_SPEED
                    elif event.key == pg.K_LEFT and abs(car.speed) > 1.25:
                        car.left = down * car.TURN_SPEED
                    elif event.key == pg.K_UP:
                        car.up = down * car.ACCELERATION_POS
                    elif event.key == pg.K_DOWN and car.speed == 0:     # car cannot go back when its going forward
                        car.down = down * -car.ACCELERATION_NEG
                    elif event.key == pg.K_LSHIFT:          # honk!
                        car.honk.play()

                # reset of car directions when key is no longer pressed
                up = event.type == pg.KEYUP
                if up:
                    if event.key == pg.K_RIGHT:
                        car.right = 0
                    elif event.key == pg.K_LEFT:
                        car.left = 0
                    elif event.key == pg.K_UP:
                        car.up = 0
                    elif event.key == pg.K_DOWN:
                        car.down = 0

            self.sprites.update()
            self.screen.fill(conf.WHITE)
            self.sprites.draw(self.screen)
            pg.display.flip()