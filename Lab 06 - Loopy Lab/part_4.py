#
import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("YA BOIS GRID THING")

done = False
clock = pygame.time.Clock()

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        
            screen.fill(WHITE)
    for y_offset in range(0, 500, 10):
        pygame.draw.rect(screen, RED,[0, 0 + y_offset, 4, 4], 3)
        for x_offset in range(0, 700, 10):
            pygame.draw.rect(screen, RED,[0 + x_offset, 0 + y_offset, 4 , 4], 3)




    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
