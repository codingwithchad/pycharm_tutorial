import pygame

# Initialize pygame
pygame.init()
WHITE = (200, 200, 200)
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 800
# Create the screen (width, height)
screen = pygame.display.set_mode((DISPLAY_HEIGHT, DISPLAY_WIDTH))
# RGB values (red, green, blue)
screen.fill((56, 25, 255))

# Title and Icon
pygame.display.set_caption("Seagull Invaders")
# icon By Freepik
icon = pygame.image.load("assets\\bird.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("assets\\space_invaders_defense.png")
playerX = 370
playerY = 480




# Game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    # <div>Icons made by Freepik from www.flaticon.com



