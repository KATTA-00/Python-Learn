'''
Snake_Food class
'''

# import module
import pygame as pg
from Details.CONSTANT import *
import time


class SingleUnit:
    UnitCount = 0

    def __init__(self, win, coordinate, color, dire="RIGHT"):
        self.width = BOX_WIDTH
        self.height = BOX_HEIGHT
        self.color = color
        self.window = win
        self.direction = dire

        self.x_value, self.y_value = coordinate
        self.gridCoodinate = (self.x_value, self.y_value)
        self.coordinate = GRID_DIC.get((self.gridCoodinate[0], self.gridCoodinate[1]))

        self.state = "READY"

        SingleUnit.UnitCount += 1
        self.Count = SingleUnit.UnitCount

    def getStarted(self):
        self.state = "STARTED"

    def showUnit(self):
        self.gridCoodinate = (self.x_value, self.y_value)
        self.coordinate = GRID_DIC.get((self.gridCoodinate[0], self.gridCoodinate[1]))
        pg.draw.rect(self.window, self.color, (self.coordinate[0], self.coordinate[1], self.width, self.height))

    def coodinateUpadate(self, new_coodinate):
        self.gridCoodinate = new_coodinate

    def getCoodinate(self):
        return self.gridCoodinate

    def colorUpdate(self, color):
        self.color = color

    def getState(self):
        return self.state

    def getCount(self):
        return self.Count

    def goRight(self):
        if self.x_value < BOX_COUNT_X - 1:
            self.x_value += 1
        else:
            self.x_value = 0

    def goLeft(self):
        if self.x_value > 0:
            self.x_value -= 1
        else:
            self.x_value = BOX_COUNT_X - 1

    def goUp(self):
        if self.y_value > 0:
            self.y_value -= 1
        else:
            self.y_value = BOX_COUNT_Y - 1

    def goDown(self):
        if self.y_value < BOX_COUNT_X - 1:
            self.y_value += 1
        else:
            self.y_value = 0

    def setDirection(self, command):

        if command == "RIGHT":
            if self.direction == "RIGHT":
                self.direction = "DOWN"
            elif self.direction == "DOWN":
                self.direction = "LEFT"
            elif self.direction == "LEFT":
                self.direction = "UP"
            elif self.direction == "UP":
                self.direction = "RIGHT"
        elif command == "LEFT":
            if self.direction == "RIGHT":
                self.direction = "UP"
            elif self.direction == "DOWN":
                self.direction = "RIGHT"
            elif self.direction == "LEFT":
                self.direction = "DOWN"
            elif self.direction == "UP":
                self.direction = "LEFT"

    @classmethod
    def getUniteCount(self):
        return SingleUnit.UnitCount


class Snake:

    def __init__(self, win, start_cood, color):
        self.lenght = 1
        self.color = color
        self.unitsObjects = []
        self.window = win
        self.start_coodinate = start_cood

        self.goTO = "right"

        self.addUnit(self.start_coodinate, self.color)

    def addUnit(self, cood, color):
        self.unitsObjects.append(SingleUnit(self.window, cood, color))

    def showSnake(self):
        for i in self.unitsObjects:
            time.sleep(0.5)
            i.showUnit()

    def getUnitsCoordinates(self):
        temp = []
        for i in self.unitsObjects:
            temp.append(tuple(i.coordinate))
        return temp

    def getSpaceCoordinate(self, grid):
        return list(set(grid) - set(self.getUnitsCoordinates()))

    def Go(self):
        for i in self.unitsObjects:
            if i.direction == "RIGHT":
                i.goRight()
            elif i.direction == "DOWN":
                i.goDown()
            elif i.direction == "LEFT":
                i.goLeft()
            elif i.direction == "UP":
                i.goUp()
