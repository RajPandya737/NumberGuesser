import pygame as pg
import numpy as np
import cv2
import random

class Map:
    def __init__(self, width, height, scale, offset):
        #Defining major components of the grid
        self.scale = scale
        self.columns = int(height/scale)
        self.rows = int(width/scale)
        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        #Grid offset is the thin line seperating the grid squares
        self.offset = offset
        #this variable is used to give unique names to files 
        self.nums = 1

    def create_array(self):
        for i in range(self.rows):
            for j in range(self.columns):
                #used to initialise grid array, helps with testing to have this here
                self.grid_array[i][j] = 1

    def gameplay(self,on,off,area):
        for i in range(self.rows):
            for j in range(self.columns):
                y_cor = j * self.scale
                x_cor = i * self.scale
                #Draws the individual rectangles based on location and if the cell is on or off
                if self.grid_array[i][j] == 0:
                    pg.draw.rect(area, on, [x_cor, y_cor, self.scale-self.offset, self.scale-self.offset])
                else:
                    pg.draw.rect(area, off, [x_cor, y_cor, self.scale-self.offset, self.scale-self.offset])

    def click(self, x,y):
        #if a cell is clicked on, it needs to update in the array of the class
        if self.grid_array[x][y] == 0:
            self.grid_array[x][y] = 1
        else: 
            self.grid_array[x][y] = 0

    def num_ones(self):
        #counts the number of on cells in the array, will change in future to allow button clicking instead
        count = 0
        for x in self.grid_array:
            for y in x:
                if y == 0:
                    count+=1
        return count

    def save_array(self):
        #saves the array by performing some geometric rotations that allign the array with the image drawn
        temp_array = np.flipud(np.rot90(255*self.grid_array))
        cv2.imwrite(f"img{self.nums}.png", temp_array)
        self.nums+=1

    def get_num(self):
        return self.nums



