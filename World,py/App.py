
import pygame as pg
import random

pg.init()

speed = 0.3
resolution_x = 800
resolution_y = 600

screen = pg.display.set_mode((resolution_x, resolution_y))
pg.display.set_caption('Space G')
icon = pg.image.load("ufo.png")
pg.display.set_icon(icon)

background = pg.image.load('Background.jpg')

battleship = pg.image.load('spaceship.png')
player_x = 300
player_y = 500
player_change = 0

enemy_look = pg.image.load('glass.png')
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 100)
enemy_changex = 0.5
enemy_changey = 20

bullet = pg.image.load('bullet.png')
bullet_state = 'ready'
bullet_x = 0
bullet_y = player_y
bullet_change = 1


def bullet_fire(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet, (x + 10, y + 15))


def player(x, y):
    screen.blit(battleship, (x, y))


def enemy(x, y):
    screen.blit(enemy_look, (x, y))


running = True

while running:
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player_change = -speed
            if event.key == pg.K_RIGHT:
                player_change = speed
            if event.key == pg.K_SPACE:
                bullet_fire(player_x, bullet_y)

        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT or event.key == pg.K_SPACE:
                player_change = 0
                bullet_x = player_x

    player_x += player_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    player(player_x, player_y)

    enemy_x += enemy_changex
    if enemy_x >= 736:
        enemy_changex = -enemy_changex
        enemy_y += enemy_changey
    elif enemy_x <= 0:
        enemy_changex = -enemy_changex
        enemy_y += enemy_changey
    enemy(enemy_x, enemy_y)

    if bullet_state == 'fire':
        bullet_fire(bullet_x,bullet_y)
        bullet_y -= bullet_change

    pg.display.update()