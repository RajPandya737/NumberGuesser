import pygame as pg
from pygame.locals import *
import tensorflow as tf
import sys
from config import *
from grid import Map
import numpy as np
import cv2

class Game:
    def __init__(self):
        #Initialise pygame and the grid 
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.caption = pg.display.set_caption('Number Guesser')
        self.clock = pg.time.Clock()
        self.Grid = Map(WIDTH, HEIGHT, SCALER, OFFSET)
        self.Grid.create_array()
        self.running = True


    def new(self):
        self.playing = True


    def update(self):
        #updates the game based on frame rate
        self.clock.tick(FPS)
        self.screen.fill(WHITE)
        self.events()
        self.Grid.gameplay(BLACK, WHITE, self.screen)
        pg.display.update()


    def events(self):
        #gets mouse and keybord input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                #Temporary solution to have the max number of mouse clicks be 9
                mx, my = pg.mouse.get_pos()
                i,j = self.get_index(mx,my)
                self.Grid.click(i,j)
                print(self.Grid.num_ones())
            if event.type == pg.KEYDOWN:
                self.Grid.save_array()
                print("saved")
                self.compute_number()
            
    
    def get_index(self, x,y):
        #Finds the x and y cordinate according to index using the mouse position
        i = x//SCALER
        j = y//SCALER
        return [i,j]
    

    def machine_learning(self):
        mnist = tf.keras.datasets.mnist
        (x_train, y_train), (x_test, y_test) = mnist.load_data()

        x_train = tf.keras.utils.normalize(x_train, axis=1)
        x_test = tf.keras.utils.normalize(x_test, axis=1)
        '''
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
        model.add(tf.keras.layers.Dense(128, activation='relu'))
        model.add(tf.keras.layers.Dense(128, activation='relu'))
        model.add(tf.keras.layers.Dense(10, activation='softmax'))

        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        model.fit(x_train, y_train, epochs=3)
        model.save('training.model')
        '''
        model = tf.keras.models.load_model('training.model')

        #loss, accuracy = model.evaluate(x_test, y_test)
        return model

    def compute_number(self):
        image_number = self.Grid.get_num()-1
        model = self.machine_learning()
        try:
            img = cv2.imread(f"img{image_number}.png")[:,:,0]
            img = np.invert(np.array([img]))
            prediction = model.predict(img)
            print(np.argmax(prediction))
        except:
            print('error')


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