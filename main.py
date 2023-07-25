import pygame as pg
from pygame.locals import *
import tensorflow as tf
import sys
from config import *
from grid import Map
import numpy as np
import cv2
from tkinter import *
from tkinter import messagebox

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
        self.clicking = False
        self.clicked_squares = []


    def new(self):
        self.playing = True


    def update(self):
        #updates the game based on frame rate
        self.clock.tick(FPS)
        self.screen.fill(WHITE)
        self.events()
        self.grid_click()
        self.Grid.gameplay(BLACK, WHITE, self.screen)
        pg.display.update()


    def events(self):
        #gets mouse and keybord input
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                #happens when mouse is held down
                if event.button == 1:
                    self.clicking = True
            elif event.type == pg.MOUSEBUTTONUP:
                #when mous button is released
                if event.button == 1:
                    self.clicking = False
                    self.clicked_squares.clear()
            if event.type == pg.KEYDOWN:
                #if a key is pressed, it signals to save the image
                self.Grid.save_array()
                print("saved")
                self.compute_number()
    

    def grid_click(self):
        if self.clicking is True:
            #if you are clicking and the position is valid, then it draws it on the board
            mx, my = pg.mouse.get_pos()
            i,j = self.get_index(mx,my)
            if (i,j) not in self.clicked_squares:
                self.clicked_squares.append((i,j))

                self.Grid.click(i,j)
                #print(self.Grid.num_ones())

            
    
    def get_index(self, x,y):
        #Finds the x and y cordinate according to index using the mouse position
        i = x//SCALER
        j = y//SCALER
        return [i,j]
    

    def machine_learning(self):
        # Loads the ML model
        model = tf.keras.models.load_model('training.model')
        return model

    def compute_number(self):
        # This is the image number, useful if a user decides to use the program multiple times
        image_number = self.Grid.get_num() - 1

        try:
            # Loads the model
            model = self.machine_learning()

            # Sets up the window message
            window = Tk()
            window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
            window.withdraw()

            try:
                img_path = f"img{image_number}.png"
                img = cv2.imread(img_path)[:, :, 0]
                if img is None:
                    raise ValueError(f"Unable to read the image: {img_path}")

                img = np.invert(np.array([img]))
                prediction = model.predict(img)
                # Shows the prediction
                messagebox.showinfo('Number', f'is your number a {np.argmax(prediction)}')
                window.deiconify()
                window.destroy()
                window.quit()
            except:
                messagebox.showerror('ERROR', f'An error has occured, please try again')
                print('error')
                print(f'An error has occured, please try again')
        except Exception as e:
            print(f'Error loading the model: {e}')




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