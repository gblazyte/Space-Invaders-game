import csv
import math
import random
import json

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("background.jpg")

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space-invaders.png")
pygame.display.set_icon(icon)

# player
playerIcon = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_move = 0

# enemy
enemyIcon = []
enemyX = []
enemyY = []
enemyX_move = []
enemyY_move = []
enemyX_move_time = 0.2
enemyY_move_time = 30

number_of_enemies = 6
#
# for i in range(number_of_enemies):
#     enemyIcon.append(pygame.image.load("invaders.png"))
#     enemyX.append(random.randint(0, 736))
#     enemyY.append(random.randint(50, 165))
#     enemyX_move.append(0.2)
#     enemyY_move.append(30)

# map generator

# with open('game_generator.csv', 'r') as csv_file:
#     spreadsheet = csv.DictReader(csv_file)
#     #number_of_enemies = 0
#     for row in spreadsheet:
#         number_of_enemies = row['num_of_enemies']

for i in range(int(number_of_enemies)):
    enemyIcon.append(pygame.image.load("invaders.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 165))
    enemyX_move.append(enemyX_move_time)
    enemyY_move.append(enemyY_move_time)

# bullet
bulletIcon = pygame.image.load("bullet.png")
bulletX = 370
bulletY = 480
bulletX_move = 0
bulletY_move = 0.6
bullet_ready = False

# item prize
random_num = 0
coinIcon = pygame.image.load("star_prize.png")
coinX = random.randint(0, 736)
coinY = 70
coinX_move = 0
coinY_move = 0.3
coin_ready = False

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# coin count
coin_value = 0
coin_font = pygame.font.Font('freesansbold.ttf', 32)

# lives count
lives_value = 3
lives_font = pygame.font.Font('freesansbold.ttf', 32)

# game over text
game_over_font = pygame.font.Font('freesansbold.ttf', 64)
game_textX = 200
game_textY = 200

# game won text
game_won_font = pygame.font.Font('freesansbold.ttf', 64)
game_textX = 200
game_textY = 200

# button to import new game
game_start_font = pygame.font.Font('freesansbold.ttf', 32)
game_start = game_start_font.render('Start', True, (255, 255, 255))
game_start_btn = pygame.Rect(650, 10, 100, 40)

# button to get lives
get_life = 2
get_lives_font = pygame.font.Font('freesansbold.ttf', 32)

# levels
level_count = 1
level_font = pygame.font.Font('freesansbold.ttf', 32)


def player(x, y):
    screen.blit(playerIcon, (x, y))


def enemy(x, y, i):
    screen.blit(enemyIcon[i], (x, y))


def fire_bullet(x, y):
    global bullet_ready
    bullet_ready = True
    screen.blit(bulletIcon, (x + 16, y + 10))


def drop_coin(x, y):
    global coin_ready
    coin_ready = True
    screen.blit(coinIcon, (x, y))


def collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


def got_coin(playerX, playerY, coinX, coinY):
    distance = math.sqrt((math.pow(playerX - coinX, 2)) + (math.pow(playerY - coinY, 2)))
    if distance < 27:
        return True
    else:
        return False


def player_score(x, y):
    score = font.render('Score : ' + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))


def coin_count(x, y):
    count = font.render('Coin count : ' + str(coin_value), True, (0, 0, 0))
    screen.blit(count, (x, y))


def lives_count(x, y):
    lives = font.render('Lives count : ' + str(lives_value), True, (0, 0, 0))
    screen.blit(lives, (x, y))


def level_text(x, y):
    levels = font.render('Level: ' + str(level_count), True, (0, 0, 0))
    screen.blit(levels, (x, y))


def get_lives(x, y):
    get_lives_sign = font.render('Get lives +', True, (0, 0, 0))
    screen.blit(get_lives_sign, (x, y))


def game_over_text(x, y):
    game_over = game_over_font.render('Game OVER!', True, (0, 0, 0))
    screen.blit(game_over, (x, y))


def game_won_text(x, y):
    game_won = game_won_font.render('You won!', True, (0, 0, 0))
    screen.blit(game_won, (x, y))


############ game loop
running = True
while running:

    screen.fill((0, 0, 0))
    # adding background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_move = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_move = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_ready is False:
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
            if event.key == pygame.K_KP_PLUS:
                if coin_value >= 2:
                    lives_value += 1
                    coin_value -= get_life
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_start_btn.collidepoint(event.pos):
                with open('game_generator.csv', 'r') as csv_file:
                    spreadsheet = csv.DictReader(csv_file)
                    for row in spreadsheet:
                        number_of_enemies = row['num_of_enemies']

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_move = 0

    # button hover effect for game start
    a, b = pygame.mouse.get_pos()
    if game_start_btn.x <= a <= game_start_btn.x + 100 and game_start_btn.y <= b <= game_start_btn.y + 40:
        pygame.draw.rect(screen, (192, 28, 226), game_start_btn)
    else:
        pygame.draw.rect(screen, (90, 0, 112), game_start_btn)

    # boundaries for player
    playerX += playerX_move
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # boundaries for enemy, enemy movement
    for i in range(int(number_of_enemies)):
        # game over
        # lives count
        if enemyY[i] > 300 and lives_value != 0:
            lives_value -= 1
            for j in range(int(number_of_enemies)):
                enemyX[j] = random.randint(0, 736)
                enemyY[j] = random.randint(50, 165)
        if lives_value == 0:
            for j in range(int(number_of_enemies)):
                enemyY[j] = 1000
            game_over_text(game_textX, game_textY)
            break


        enemyX[i] += enemyX_move[i]

        if enemyX[i] <= 0:
            enemyX_move[i] = enemyX_move_time
            enemyY[i] += enemyY_move[i]
        elif enemyX[i] >= 736:
            enemyX_move[i] = -enemyX_move_time
            enemyY[i] += enemyY_move[i]

        # check if enemy collided with the bullet
        is_collision = collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if is_collision:
            bulletY = 480
            coinY = 70
            bullet_ready = False
            coin_ready = False
            score_value += 1
            # print(score_value)
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 165)
            # drop coin
            random_num = random.randint(0, 100)
            # print(random_num)
            if 0 <= random_num <= 50:
                if coin_ready is False:
                    coinX = random.randint(0, 736)
                    drop_coin(coinX, coinY)

        enemy(enemyX[i], enemyY[i], i)

    # check if the spaceship got the coin
    is_got_coin = got_coin(playerX, playerY, coinX, coinY)
    if is_got_coin:
        coinY = 70
        coin_ready = False
        coin_value += 1
        #print(coin_value)

    # Shooting a bullet
    if bulletY <= 0:
        bulletY = 480
        bullet_ready = False

    if bullet_ready is True:
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_move

    # dropping a coin
    if coinY <= 0:
        coinY = 70
        coin_ready = False

    if coin_ready is True:
        drop_coin(coinX, coinY)
        coinY += coinY_move

    # level change
    if score_value == 2 and level_count == 1:
        level_count += 1
        enemyX_move_time += 0.1
        enemyY_move_time -= 5
    elif score_value == 4 and level_count == 2:
        level_count += 1
        enemyX_move_time += 0.1
        enemyY_move_time -= 5
    elif score_value == 6 and level_count == 3:
        level_count += 1
        enemyX_move_time += 0.1
        enemyY_move_time -= 5
    elif score_value == 8 and level_count == 4:
        level_count += 1
        enemyX_move_time += 0.1
        enemyY_move_time -= 5
    elif score_value == 10 and level_count == 5:
        level_count += 1
        enemyX_move_time += 0.1
        enemyY_move_time -= 5
    elif score_value == 12 and level_count == 6:
        level_count += 1
        enemyX_move_time += 0.1
        enemyY_move_time -= 5

    if level_count == 6:
        print("You won the game!")
        break


    player(playerX, playerY)

    player_score(10, 10)

    coin_count(10, 50)

    lives_count(10, 90)

    get_lives(10, 140)

    level_text(620, 60)

    screen.blit(game_start, (game_start_btn.x + 5, game_start_btn.y + 5))

    pygame.display.update()

# saving players scores to json

player_name = input("What is your name? ")

player_dict = {}

player_dict[player_name] = {'score': score_value}

with open('mydata.json', 'r') as file:
    player_dict = json.load(file)
    player_dict[player_name] = {'score': score_value}

with open('mydata.json', 'w') as file:
    file.write(json.dumps(player_dict))
