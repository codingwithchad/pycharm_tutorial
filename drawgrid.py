def drawGrid():
    block_size = 20
    for x in range(DISPLAY_WIDTH):
        for y in range(DISPLAY_HEIGHT):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            pygame.draw.rect(screen, WHITE, rect, 1)