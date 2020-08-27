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

# Player
player_img = pygame.image.load("assets\\space_invaders_defense.png")
player_x = DISPLAY_WIDTH / 2
player_y = ((DISPLAY_HEIGHT / 4)*3)

# Fill the screen with a color
# Objects render in order, screen.fill should be first
screen.fill(SKY_BLUE)
# Title and Icon
pygame.display.set_caption("Seagull Invaders")
# icon By Freepik
icon = pygame.image.load("assets\\bird.png") # Icons made by Freepik from www.flaticon.com
pygame.display.set_icon(icon)

# Game loop
running = True

# Function to add the player to the screen
def player0():
    screen.blit(player_img, (player_x, player_y))


while running:

    # Keeps the loop from being infinite.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calls the player function
    player0()
    pygame.display.update()




