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

    # Fill the screen with a color
    # Objects render in order, screen.fill should be first
    screen.fill(SKY_BLUE)

    # Calls the player function
    player_y -= 0.01

    player0(player_x, player_y)
    pygame.display.update()




