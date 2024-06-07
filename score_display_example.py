import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dynamic Text Example")

# Define constant colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load font
font = pygame.font.Font(None, 32)  # None uses the default font, 32 is the font size

# Initialize score
score = 0

# Render initial score text
score_text = f"Score: {score}"  # We use f-strings here for formatting variables
score_surface = font.render(score_text, True, WHITE)
score_rect = score_surface.get_rect()
score_rect.topleft = (10, 10)

clock = pygame.time.Clock()

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:  # Press SPACE to increase score
                score += 1  # Update score and re-render text surface starts here
                score_text = f"Score: {score}"  
                score_surface = font.render(score_text, True, WHITE)

    # Fill the screen with black
    screen.fill(BLACK)
    
    # Draw updated score
    screen.blit(score_surface, score_rect)
    
    # Update display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()