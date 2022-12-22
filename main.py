import pygame as pg
import numpy as np
import os
import sys
from math import sqrt
from config import *
from grid import Map


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.caption = pg.display.set_caption('Number Guesser')
        self.clock = pg.time.Clock()
        self.Grid = Map(WIDTH, HEIGHT, SCALER, OFFSET)
        self.Grid.rand_array()
        self.running = True


    def new(self):
        self.playing = True


    def update(self):
        self.clock.tick(FPS)
        self.screen.fill(BLUE)
        self.events()
        self.Grid.gameplay(WHITE, BLACK, self.screen)
        pg.display.update()


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN and self.Grid.num_ones()<9:
                mx, my = pg.mouse.get_pos()
                i,j = self.get_index(mx,my)
                self.Grid.click(i,j)
                print(self.Grid.num_ones())
            if event.type == pg.MOUSEBUTTONDOWN and self.Grid.num_ones()==9:
                mx, my = pg.mouse.get_pos()
                i,j = self.get_index(mx,my)
                self.Grid.click(i,j)
                self.Grid.save_array()
    
    def get_index(self, x,y):
        i = x//SCALER
        j = y//SCALER
        return [i,j]



    def main(self):
        #runs the game
        while self.playing is True:
            self.update()
        self.running = False


if __name__ == '__main__':
    game = Game()
    game.new()
    while game.running:
        game.main()
    pg.quit()
    sys.exit()