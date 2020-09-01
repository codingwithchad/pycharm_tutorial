import pygame
import random
import math

# Initialize pygame
pygame.init()

# COLORS RGB
WHITE = (200, 200, 200)
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
enemy_img = pygame.image.load("assets\\bird.png")  # Icons made by Freepik from www.flaticon.com
enemy_x = random.randint(LEFT_BOUND, RIGHT_BOUND - 86)
enemy_y = random.randint(50, 150)
enemy_speed = 2  # Speed
enemy_x_change = enemy_speed
enemy_y_change = 40

# balloon
# Ready state - you can't see the balloon on the screen
# Fire state - The balloon is moving
balloon_img = pygame.image.load("assets\\balloon.png")  # Icons made by Freepik from www.flaticon.com
balloon_x = 0
balloon_y = DISPLAY_HEIGHT - 86
balloon_speed = 4  # Speed
balloon_y_change = balloon_speed
balloon_state = "ready"

score = 0

# Game loop
running = True


# Function to add the player to the screen
def player0(x, y):
    screen.blit(player_img, (x, y))


# Function to add the enemy to the screen
def enemy0(x, y):
    screen.blit(enemy_img, (x + 16, y + 10))


# Function to add the enemy to the screen
def release_balloon(x, y):
    global balloon_state
    balloon_state = "fire"
    screen.blit(balloon_img, (x, y))


def isCollision(enemyX, enemyY, balloonX, balloonY):
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
    enemy_x += enemy_x_change
    if enemy_x >= RIGHT_BOUND:
        enemy_x_change = enemy_speed * -1
        enemy_y += enemy_y_change
    elif enemy_x <= LEFT_BOUND:
        enemy_x_change = enemy_speed
        enemy_y += enemy_y_change

    # Reset the balloon when the balloon reaches the top of the screen
    if balloon_y <= 0:
        balloon_y = 480
        balloon_state = "ready"

    # Balloon movement
    if balloon_state is "fire":
        release_balloon(balloon_x, balloon_y)
        balloon_y -= balloon_y_change

    # Collision
    collision = isCollision(enemy_x, enemy_y, balloon_x, balloon_y)
    if collision:
        balloon_y = 480
        balloon_state = "ready"
        score += 100
        enemy_x = random.randint(LEFT_BOUND, RIGHT_BOUND - 36)
        enemy_y = random.randint(50, 150)
        print(score)
    player0(player_x, player_y)
    enemy0(enemy_x, enemy_y)
    pygame.display.update()
