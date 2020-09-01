'''
I am learning pygames by following along with the video https://www.youtube.com/watch?v=FfWpgLFMI7w
The original code can be found https://github.com/attreyabhatt/Space-Invaders-Pygame
I changed the aliens to seagulls and bullets to balloons.
'''
import random
import math

import pygame
from pygame import mixer

# Initialize pygame
pygame.init()

# COLORS RGB
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)

# Display size
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
RIGHT_BOUND = 736
LEFT_BOUND = 0

# Create the screen (width, height)
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# Background
background = pygame.image.load("assets\\beach-background.jpg")

# Background Sound
mixer.music.load("assets\\background.wav")
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Seagull Invaders")
icon = pygame.image.load("assets\\bird.png")  # Icons made by Freepik from www.flaticon.com
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load("assets\\space_invaders_defense.png")  # Icons made by Freepik from www.flaticon.com
player_x = DISPLAY_WIDTH / 2
player_y = DISPLAY_HEIGHT - 86
player_x_change = 0
player_speed = 3  # Speed

# Enemy
enemy_img = []
enemy_x = []
enemy_y = []
enemy_y_change = 40
num_enemies = 6
enemy_speed = 1.5  # Speed

enemy_x_change = enemy_speed
for i in range(num_enemies):
    enemy_img.append(pygame.image.load("assets\\bird.png"))  # Icons made by Freepik from www.flaticon.com
    enemy_x.append(random.randint(LEFT_BOUND + 45, (RIGHT_BOUND - 86) - 45))
    enemy_y.append(random.randint(50, 150))

# balloon
# Ready state - you can't see the balloon on the screen
# Fire state - The balloon is moving
balloon_img = pygame.image.load("assets\\balloon.png")  # Icons made by Freepik from www.flaticon.com
balloon_x = 0
balloon_y = DISPLAY_HEIGHT - 86
balloon_speed = 4  # Speed
balloon_y_change = balloon_speed
balloon_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

# Game loop
running = True


# Function to add the player to the screen
def player0(x, y):
    screen.blit(player_img, (x, y))


# Function to add the enemy to the screen
def enemy0(x, y, i):
    screen.blit(enemy_img[i], (x + 16, y + 10))


# Function to add the enemy to the screen
def release_balloon(x, y):
    global balloon_state
    balloon_state = "fire"
    screen.blit(balloon_img, (x, y))


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, BLACK)
    screen.blit(score, (x, y))


def is_collision(enemyX, enemyY, balloonX, balloonY):
    distance = math.sqrt((math.pow(enemyX - balloonX, 2)) + (math.pow(enemyY - balloonY, 2)))
    if distance < 27:
        return True
    return False


while running:

    # Keeps the loop from being infinite.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #  If keystroke is pressed, check if left arrow or right arrow
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = player_speed * -1
            if event.key == pygame.K_RIGHT:
                player_x_change = player_speed
            if event.key == pygame.K_SPACE and balloon_state == "ready":
                balloon_x = player_x  # Get the current location of the player, but don't change with the player
                release_balloon(balloon_x, balloon_y)
                bullet_sound = mixer.Sound("assets\\laser.wav")
                bullet_sound.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player_x_change = 0

    # Fill the screen with a color
    # Objects render in order, screen.fill should be first
    screen.fill(SKY_BLUE)
    screen.blit(background, (0, 0))

    # Check for boundaries for player so it doesn't go off the screen
    player_x += player_x_change
    if player_x >= RIGHT_BOUND:
        player_x = RIGHT_BOUND
    elif player_x <= LEFT_BOUND:
        player_x = LEFT_BOUND

    # Enemy movement
    for i in range(num_enemies):
        enemy_x[i] += enemy_x_change
        if enemy_x[i] >= RIGHT_BOUND:
            enemy_x_change = enemy_speed * -1
            for y in range(num_enemies):
                enemy_y[y] += enemy_y_change
        elif enemy_x[i] <= LEFT_BOUND:
            enemy_x_change = enemy_speed
            for y in range(num_enemies):
                enemy_y[y] += enemy_y_change
        if enemy_y[i] >= DISPLAY_HEIGHT:
            enemy_x[i] = random.randint(LEFT_BOUND, RIGHT_BOUND - 36)
            enemy_y[i] = random.randint(50, 150)
        enemy0(enemy_x[i], enemy_y[i], i)
        # Collision
        collision = is_collision(enemy_x[i], enemy_y[i], balloon_x, balloon_y)
        if collision:
            balloon_y = 480
            balloon_state = "ready"
            score_value += 100
            enemy_x[i] = random.randint(LEFT_BOUND, RIGHT_BOUND - 36)
            enemy_y[i] = random.randint(50, 150)
            explosion_sound = mixer.Sound("assets\\explosion.wav")
            explosion_sound.play()

    # Reset the balloon when the balloon reaches the top of the screen
    if balloon_y <= 0:
        balloon_y = 480
        balloon_state = "ready"

    # Balloon movement
    if balloon_state is "fire":
        release_balloon(balloon_x, balloon_y)
        balloon_y -= balloon_y_change

    player0(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()
