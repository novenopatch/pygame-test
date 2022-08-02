import sys

import pygame

pygame.init()

screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()

testSurface = pygame.Surface((100,200))
testSurface.fill((0,0,255))
testRect = testSurface.get_rect(topright=(200,250))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    screen.fill((175,215,70))
    testRect.y -=1
    screen.blit(testSurface,testRect)
    pygame.display.update()
    clock.tick(60)
