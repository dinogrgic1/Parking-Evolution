import pygame as pg
import conf
import src.Car as Car
import src.Map as Map
import src.ParkSapce as ParkSpace


class Game:
    def __init__(self):
        pg.init()  # initialization of pg module
        pg.mixer.init()  # initialization of mixer used for sounds in a game
        self.screen = pg.display.set_mode((conf.WIDTH, conf.HEIGHT), pg.HWSURFACE | pg.DOUBLEBUF | pg.RESIZABLE)
        self.font = pg.font.SysFont(conf.FONT, 30)
        pg.display.set_caption(conf.CAPTION)  # screen title
        self.clock = pg.time.Clock()  # game clock
        self.change = 0

        self.sprites = None
        self.parked = 0
        self.score = 0
        self.score_text = None
        self.fps_text = None
        self.running = True

    # initalization of game object
    def init(self):
        self.sprites = pg.sprite.Group()  # initialise group of sprites
        global car
        global bg
        global ps

        car = Car.Car()     # TODO : this is stupid
        bg = Map.Map()
        ps = ParkSpace.ParkSpace(bg.BORDER)
        self.sprites.add(bg, ps, car)

    def game_loop(self):
        while self.running:
            self.init()
            self.done = False
            while not self.done:
                self.clock.tick(conf.FPS)  # FPS argument of tick() is how many frames per second we want
                # EVENT LOGIC : event - handling loop
                for event in pg.event.get():  # go through list of events per second
                    if event.type == pg.QUIT:   # look if user closed the window
                        self.running = False # TODO: change the way you exit game loop
                        self.done = True

                    elif event.type == pg.VIDEORESIZE:
                        self.screen = pg.display.set_mode(
                            event.dict['size'], pg.HWSURFACE | pg.DOUBLEBUF | pg.RESIZABLE)
                        self.screen.blit(pg.transform.scale(car.image, event.dict['size']), car.rect.center)
                        pg.display.flip()

                    down = event.type == pg.KEYDOWN
                    if down:
                        if event.key == pg.K_RIGHT and abs(car.speed) > 1.25:       # car cannot turn R with a small speed
                            car.right = down * -car.TURN_SPEED
                        elif event.key == pg.K_LEFT and abs(car.speed) > 1.25:      # car cannot turn L with a small speed
                            car.left = down * car.TURN_SPEED
                        elif event.key == pg.K_UP and car.speed >= 0:       # car cannot go forward when its going back
                            car.up = down * car.ACCELERATION_POS
                        elif event.key == pg.K_DOWN and car.speed <= 0:     # car cannot go back when its going forward
                            car.down = down * -car.ACCELERATION_NEG
                        elif event.key == pg.K_LSHIFT:          # honk!
                            car.honk.play()
                        elif event.key == pg.K_F1:          # pick colors of a car
                            car.color_pick('blue')
                        elif event.key == pg.K_F2:
                            car.color_pick('green')
                        elif event.key == pg.K_F3:
                            car.color_pick('pink')
                        elif event.key == pg.K_F4:
                            car.color_pick('red')
                        elif event.key == pg.K_F12:
                            self.done = True

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

                # check car collision with the white border
                hit_ver = car.rect.top <= bg.BORDER_TOP or car.rect.bottom >= bg.BORDER_BOTTOM
                hit_hor = car.rect.left <= bg.BORDER_LEFT or car.rect.right >= bg.BORDER_RIGHT
                if hit_ver or hit_hor:
                    self.done = True

                self.score = ps.parked(car)
                self.score_text = self.font.render(conf.SCORE_TEXT + str(self.score), False, conf.BLACK)
                self.fps_text = self.font.render('FPS : ' + (str(int(self.clock.get_fps()))), False, conf.BLACK)

                self.sprites.update()
                self.screen.fill(conf.WHITE)
                self.sprites.draw(self.screen)

                self.screen.blit(self.score_text, (0, 0))
                self.screen.blit(self.fps_text, (conf.WIDTH - 100, 0))
                pg.display.flip()

