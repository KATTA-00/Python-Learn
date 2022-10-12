'''
Egg class
'''

# import modules
from Details.CONSTANT import *
import pygame as pg
import random


class Egg:

    def __init__(self, win, cood, color, time):
        self.window = win
        self.coordinate = cood
        self.color = color
        self.width = BOX_WIDTH
        self.height = BOX_HEIGHT
        self.time = time

    def showEgg(self):
        pg.draw.rect(self.window, self.color, (self.coordinate[0], self.coordinate[1], self.width, self.height))

    def changeTime(self, change=0):
        if change != 0:
            self.time = change

    def changeCooordinates(self,space):
        self.coordinate = random.choice(space)



