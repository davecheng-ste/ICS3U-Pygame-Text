"""
Author: D. Cheng
Date: 2024-06-06
Description: Pygame ocean tech demo with collisions and score, refactored for readability.
"""

import pygame
import sys
import random

# Define constants
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SHRIMP_SPEED = 10
SHARK_SPEED = 8
SHARK_FRAME_DURATION = 250  # Frame duration in milliseconds (ms)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Ocean")
clock = pygame.time.Clock()

# Define all game functions
def load_assets():
    """
    Load all graphics assets for the game.
    """
    background = pygame.image.load("images/water_background.png")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    shrimp_image = pygame.image.load("images/shrimp.png")
    shark_frames = [
        pygame.image.load("images/shark01.png"),
        pygame.image.load("images/shark02.png")
    ]
    return background, shrimp_image, shark_frames


def init_text():
    """
    Initialize text surfaces and rectangles for instructions and score display.
    """
    font_instructions = pygame.font.Font(None, 18)
    text_instructions_string = "WASD to move shark. Catch as many shrimp as you can!"
    text_instructions_surface = font_instructions.render(text_instructions_string, True, WHITE)
    text_instructions_rect = text_instructions_surface.get_rect(center=(WIDTH // 2, HEIGHT - 10))

    font_score = pygame.font.Font(None, 32)
    text_score_surface = font_score.render("Score: 0", True, WHITE)
    text_score_rect = text_score_surface.get_rect(topleft=(10, 10))

    return text_instructions_surface, text_instructions_rect, font_score, text_score_surface, text_score_rect


def init_game_elements():
    """
    Initialize game elements like the shrimp and shark rectangles.
    """
    shrimp_rect = shrimp_image.get_rect(left=WIDTH, centery=100)
    shark_rect = shark_frames[0].get_rect(center=(WIDTH // 2, HEIGHT // 2))
    return shrimp_rect, shark_rect


def handle_input():
    """
    Handle user inputs such as quit and movement keys.
    """
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False


def update_game_state():
    """
    Update the game state including positions of shark and shrimp, and handle collisions.
    """
    global shrimp_rect, shark_rect, player_score, text_score_surface, shark_frame_index, shark_time_changed

    # Refresh sprite animation frames
    time_now = pygame.time.get_ticks()
    if time_now - shark_time_changed > SHARK_FRAME_DURATION:
        shark_frame_index = (shark_frame_index + 1) % len(shark_frames)
        shark_time_changed = time_now

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and shark_rect.top >= 0:
        shark_rect.y -= SHARK_SPEED
    elif keys[pygame.K_s] and shark_rect.bottom <= HEIGHT:
        shark_rect.y += SHARK_SPEED
    if keys[pygame.K_d] and shark_rect.right <= WIDTH:
        shark_rect.x += SHARK_SPEED
    elif keys[pygame.K_a] and shark_rect.left >= 0:
        shark_rect.x -= SHARK_SPEED

    # Handle shrimp movement
    if shrimp_rect.right >= 0:
        shrimp_rect.x -= SHRIMP_SPEED
    else:
        shrimp_rect.left = WIDTH
        shrimp_rect.centery = random.randint(20, HEIGHT - 20)

    # Handle shark and shrimp collisions
    if shark_rect.colliderect(shrimp_rect):
        # Respawn shrimp
        shrimp_rect.left = WIDTH
        shrimp_rect.centery = random.randint(20, HEIGHT - 20)
        # Update score and rerender surface
        player_score += 1
        text_score_surface = font_score.render(f"Score: {player_score}", True, WHITE)


def draw():
    """
    Draw all game elements on the screen.
    """
    screen.blit(background, (0, 0))
    screen.blit(shark_frames[shark_frame_index], shark_rect)
    screen.blit(shrimp_image, shrimp_rect)
    screen.blit(text_instructions_surface, text_instructions_rect)
    screen.blit(text_score_surface, text_score_rect)
    pygame.display.flip()


# Initialize game using function calls
background, shrimp_image, shark_frames = load_assets()
text_instructions_surface, text_instructions_rect, font_score, text_score_surface, text_score_rect = init_text()
shrimp_rect, shark_rect = init_game_elements()

# Initialize game start conditions
player_score = 0
shark_frame_index = 0
shark_time_changed = pygame.time.get_ticks()

# Run main game loop
running = True

while running:
    handle_input()
    update_game_state()
    draw()
    clock.tick(30)

pygame.quit()
sys.exit()
