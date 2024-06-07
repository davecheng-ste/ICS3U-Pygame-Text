import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Text Handling")

# Define constant colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load font
font = pygame.font.Font("fonts/GummyBear.ttf", 48)  # Font is in a folder, fonts/GummyBear.ttf 

# Render text
text_string = "Hello, Pygame!"
text_colour = WHITE
text_surface = font.render(text_string, True, text_colour)  # True for anti-aliasing

# Get text rectangle
text_rect = text_surface.get_rect()

# Position text
text_rect.center = (WIDTH // 2, HEIGHT // 2)  # Center of the screen

clock = pygame.time.Clock()

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill(BLACK)
    
    # Draw text
    screen.blit(text_surface, text_rect)
    
    # Update display
    pygame.display.flip()
    clock.tick(30)

# Quit Pygame
pygame.quit()
sys.exit()