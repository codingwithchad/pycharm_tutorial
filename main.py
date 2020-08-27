import pygame

# Initialize pygame
pygame.init()

# Create the screen (width, height)
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Seagull Invaders")
# icon By Freepik
icon = pygame.image.load("assets\\bird.png")
pygame.display.set_icon(icon)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RGB values (red, green, blue)
    screen.fill((56, 25, 255))
    pygame.display.update()
    # <div>Icons made by Freepik from www.flaticon.com
