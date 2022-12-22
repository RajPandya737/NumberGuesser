import pygame as pg
import numpy as np
import cv2
import random

class Map:
    def __init__(self, width, height, scale, offset):
        self.scale = scale
        self.columns = int(height/scale)
        self.rows = int(width/scale)
        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset
        self.nums = 1

    def rand_array(self):
        for i in range(self.rows):
            for j in range(self.columns):
                #Infuture, get user input and place it into here
                self.grid_array[i][j] = 0

    def gameplay(self,on,off,area):
        for i in range(self.rows):
            for j in range(self.columns):
                y_cor = j * self.scale
                x_cor = i * self.scale

                if self.grid_array[i][j] == 1:
                    pg.draw.rect(area, on, [x_cor, y_cor, self.scale-self.offset, self.scale-self.offset])
                else:
                    pg.draw.rect(area, off, [x_cor, y_cor, self.scale-self.offset, self.scale-self.offset])

    def click(self, x,y):
        if self.grid_array[x][y] == 1:
            self.grid_array[x][y] = 0
        else: 
            self.grid_array[x][y] = 1

    def num_ones(self):
        count = 0
        for x in self.grid_array:
            for y in x:
                if y == 1:
                    count+=1
        return count

    def save_array(self):
        temp_array = self.grid_array

        
        cv2.imwrite(f"user_number_{self.nums}.png", temp_array)
        self.nums+=1


    

