import pygame as pg
import random

pg.init()

point = 0
point_limite = 5
speed = 0.3
resolution_x = 800
resolution_y = 600

screen = pg.display.set_mode((resolution_x, resolution_y))
pg.display.set_caption('Space G')
icon = pg.image.load("ufo.png")
pg.display.set_icon(icon)

battleship = pg.image.load('spaceship.png')
player_x = 300
player_y = 500
player_change = 0

enemy_look = pg.image.load('glass.png')
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 100)
enemy_y_uplim = 50
enemy_y_dowmlim = 100
enemy_changex = 0.1
enemy_changey = 0.05


def player(x, y):
    screen.blit(battleship, (x, y))


def enemy(x, y):
    screen.blit(enemy_look, (x, y))


running = True

while running:
    screen.fill((0, 0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player_change = -speed
            if event.key == pg.K_RIGHT:
                player_change = speed
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                player_change = 0

    player_x += player_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    player(player_x, player_y)

    if enemy_x - 1 < player_x <= enemy_x + 1:
        point += 1
        enemy_x = random.randint(0, 736)
        enemy_y = random.randint(enemy_y_uplim, enemy_y_dowmlim)

    enemy_x += enemy_changex
    enemy_y += enemy_changey
    if enemy_x >= 736:
        enemy_changex = -enemy_changex
        enemy_y += enemy_changey
    elif enemy_x <= 0:
        enemy_changex = -enemy_changex
        enemy_y += enemy_changey

    if point > point_limite:
        speed += 0.1
        point_limite += 5
        enemy_y_uplim += 20
        enemy_y_dowmlim += 20
    enemy(enemy_x, enemy_y)
    pg.display.update()
