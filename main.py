import pygame

# Initialize pygame
pygame.init()

# COLORS RGB
WHITE = (200, 200, 200)
SKY_BLUE = (135, 206, 235)

# Display size
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
# Create the screen (width, height)
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))


# Title and Icon
pygame.display.set_caption("Seagull Invaders")
icon = pygame.image.load("assets\\bird.png")  # Icons made by Freepik from www.flaticon.com
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load("assets\\space_invaders_defense.png")  # Icons made by Freepik from www.flaticon.com
player_x = DISPLAY_WIDTH / 2
player_y = ((DISPLAY_HEIGHT / 4)*3)
player_x_change = 0
player_speed = 0.15  # Speed

# Game loop
running = True


# Function to add the player to the screen
def player0(x, y):
    screen.blit(player_img, (x, y))


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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player_x_change = 0

    # Fill the screen with a color
    # Objects render in order, screen.fill should be first
    screen.fill(SKY_BLUE)

    # Calls the player function

    player_x += player_x_change
    if player_x >= 736:
        player_x = 736
    elif player_x <= 0:
        player_x = 0
    player0(player_x, player_y)
    pygame.display.update()




