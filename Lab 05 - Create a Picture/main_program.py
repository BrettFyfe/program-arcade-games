# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()

#Color Variables
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

PI = 3.141592653

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("YA Bois color adventure ")

done = False
clock = pygame.time.Clock()

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    pygame.draw.line(screen, RED, [0, 0], [700, 0], 25)
    pygame.draw.rect(screen, BLUE, [0, 11 ,250,100], 10)
    pygame.draw.rect(screen, BLACK, [10, 20, 230, 90], 10)
    pygame.draw.line(screen, GREEN, [255, 25], [700, 25], 25)
    pygame.draw.line(screen, RED, [255, 50], [700, 50], 25)
    pygame.draw.line(screen, BLUE, [255, 75], [700, 75], 25)
    pygame.draw.line(screen, BLACK, [255, 100], [700, 100], 25)
    pygame.draw.line(screen, RED, [15, 35], [235, 35], 20)
    pygame.draw.line(screen, BLUE, [0, 125], [700, 125], 25)
    pygame.draw.line(screen, GREEN, [0, 150], [700, 150], 50)
    pygame.draw.line(screen, RED, [0, 200], [700, 200], 50)
    pygame.draw.line(screen, BLUE, [0, 250], [700, 250], 50)
    pygame.draw.line(screen, GREEN, [0, 300], [700, 300], 50)
    pygame.draw.line(screen, RED, [0, 350], [700, 350], 100)
    pygame.draw.line(screen, BLUE, [0, 450], [700, 450], 100)
    
    
    font = pygame.font.SysFont('Calibri', 40, True, False)
    text = font.render("Sleep",True, BLACK)
    screen.blit(text, [80,60])
    screen.blit(text, [200, 150])
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
