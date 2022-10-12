from Board.BOARD import Board
from Snake_Food.SNAKE_BODY import Snake
from Snake_Food.FOOD import Egg
from Details.CONSTANT import *
from Engine.ENGINE import Engine
import pygame as pg
import time
import random

#WINDOW
WINDOW = Board(NAME, (HEIGHT, WIDTH))
snake = Snake(WINDOW.Window,(2,2),black)
snake.addUnit((1,2),black)


#EGG
egg = Egg(WINDOW.Window,snake.getSpaceCoordinate(GRID_POINTS),red,12)
egg.changeCooordinates(snake.getSpaceCoordinate(GRID_POINTS))
egg.showEgg()

#COMMAND
COMMAND = None
STARTED = False

#TIME Delay
TIME_STEP = 0.5

#main loop
while True:

    for event in pg.event.get():

        if event.type == pg.QUIT:
            exit()

        if event.type == pg.KEYDOWN:

            if event.key == pg.K_SPACE:
                COMMAND = "START"
                STARTED = True

            elif event.key == pg.K_RIGHT:
                COMMAND = "RIGHT"
                #SNAKE_PATH.append(COMMAND)
                snake.unitsObjects[0].setDirection(COMMAND)

            elif event.key == pg.K_LEFT:
                COMMAND = "LEFT"
                #SNAKE_PATH.append(COMMAND)
                snake.unitsObjects[0].setDirection(COMMAND)


    print(SNAKE_PATH)
    Engine(SNAKE_PATH,snake.unitsObjects)
    WINDOW.resetScreen()
    WINDOW.gridOn()

    egg.showEgg()

    snake.Go()
    snake.showSnake()

    pg.display.update()
    time.sleep(TIME_STEP)