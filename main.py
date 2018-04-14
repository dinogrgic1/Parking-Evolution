import pygame as pg
import src.Game as game

if __name__ == '__main__':
    app = game.Game()
    app.game_loop()
    pg.quit()
    quit()