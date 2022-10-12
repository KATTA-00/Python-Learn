import pygame as pg
import random
import math

pg.init()

speed = 0.3
resolution_x = 800
resolution_y = 600
score = 0

screen = pg.display.set_mode((resolution_x, resolution_y))
pg.display.set_caption('Space G')
icon = pg.image.load("ufo.png")
pg.display.set_icon(icon)

background = pg.image.load('Background.jpg')

battleship = pg.image.load('spaceship.png')
player_x = 300
player_y = 500
player_change = 0

enemy_look = []
enemy_x = []
enemy_y = []
enemy_changex = []
enemy_changey = []
number_en = 6
for i in range(number_en):
    enemy_look.append(pg.image.load('glass.png'))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 100))
    enemy_changex.append(0.5)
    enemy_changey.append(20)

bullet = pg.image.load('bullet.png')
bullet_state = 'ready'
bullet_x = 0
bullet_y = player_y
bullet_change = 1

font = pg.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10


def score_show(x, y):
    sco = font.render("score : " + str(score), True, (255, 255, 255))
    screen.blit(sco, (x, y))

oever_font = pg.font.Font('freesansbold.ttf', 64)

def game_over():
    over = oever_font.render("GAME OVER!!!!!",True,(255,255,255))
    screen.blit(over,(200,250))


def bullet_fire(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet, (x + 10, y + 15))


def player(x, y):
    screen.blit(battleship, (x, y))


def enemy(x, y, i):
    screen.blit(enemy_look[i], (x, y))


def distance(x1, y1, x2, y2):
    dis = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if dis < 27:
        return True
    else:
        return False


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
            if event.key == pg.K_SPACE and bullet_state == 'ready':
                bullet_x = player_x
                bullet_fire(bullet_x, bullet_y)
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                player_change = 0

    player_x += player_change
    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736
    player(player_x, player_y)

    for i in range(number_en):

        if enemy_y[i] > 200:
            for j in range(number_en):
                enemy_y[j] = 2000
            game_over()
            break

        enemy_x[i] += enemy_changex[i]
        if enemy_x[i] >= 736:
            enemy_changex[i] = -enemy_changex[i]
            enemy_y[i] += enemy_changey[i]
        elif enemy_x[i] <= 0:
            enemy_changex[i] = -enemy_changex[i]
            enemy_y[i] += enemy_changey[i]
        enemy(enemy_x[i], enemy_y[i], i)

        if distance(enemy_x[i], enemy_y[i], bullet_x, bullet_y):
            bullet_y = player_y
            bullet_state = 'ready'
            score += 1
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(50, 100)

    if bullet_y <= 20:
        bullet_state = 'ready'
        bullet_y = player_y
    if bullet_state == 'fire':
        bullet_fire(bullet_x, bullet_y)
        bullet_y -= bullet_change
    score_show(text_x, text_y)
    pg.display.update()
