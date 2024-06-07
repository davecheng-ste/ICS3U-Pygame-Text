# Displaying Text in Pygame
Whether it is a score, timer, or instructions for the player, displaying text is a fundamental part of many Pygame projects. Here is a primer on how to work with text. 

![screenshot](images/screenshot01.png)

## Loading and Rendering Text
To render text in Pygame, we have to follow these steps:

- **Load a Font**: You can use the default font or specify a font file to load.
- **Render Text**: Convert the text string into an image, i.e., a Pygame surface.
- **Blit the Text**: Draw or "blit" the text surface onto the screen.

### Step 1: Loading a Font
You can load a font using `pygame.font.Font()`. To use the default system font, pass `None` as the first argument. The second argument is the **font size**.

```python
# Load font
font = pygame.font.Font(None, 32)  # None uses the default font, 32 is the font size
```

If you have a specific font file, provide the path to the file:

```python
font = pygame.font.Font("path/to/font.ttf", 32)  # Replace with the path to your font file
```

### Step 2: Rendering Text
Use the render method to convert a text string into a Pygame surface. You can specify the colour and other settings like anti-aliasing (font smoothing).

```python
# Render text
text_string = "Hello, Pygame!"
text_colour = WHITE
text_surface = font.render(text_string, True, text_colour)  # True for anti-aliasing
```

### Step 3: Positioning Text
To position the text, create a `Rect` object to blit and position your rendered text. 

```python
# Get text rectangle
text_rect = text_surface.get_rect()

# Position text
text_rect.center = (WIDTH // 2, HEIGHT // 2)  # Center of the screen
```

Remember, you can use many of the `Rect` methods to position the text. For example, we can also specify the aboslute position of the *top left* corner of `text_rect` using:

```python
# Position text 20 pixels in from top-left corner of screen
text_rect.x = 20
text_rect.y = 20
```

### Step 4: Blitting the Text
Finally, draw the text surface onto the screen:

```python
# Draw text
screen.blit(text_surface, text_rect)
```

### Full Example
Here's a complete example incorporating all the steps:

```python
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
font = pygame.font.Font(None, 32)  # None uses the default font, 32 is the font size

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
```

<br><br>

## Changing Font Size and Font Type
You can easily change the font size and type by modifying the arguments in `pygame.font.Font()`. 

For example, to use a different font and size:

```python
# Load a specific font with a different size
font = pygame.font.Font("path/to/your/font.ttf", 24)
```

Pygame should be able to support a variety of font formats, includingn TrueType (`.TTF`), OpenType (`.OTF`), and PostScript (`.PS`).

<br><br>

## Handling Multiple Texts
To display multiple texts, repeat the rendering and blitting steps for each text item. 

```python
# Load font
font_small = pygame.font.Font(None, 24)
font_large = pygame.font.Font(None, 48)

# Render texts
text1_surface = font_small.render("Small Text", True, WHITE)
text2_surface = font_large.render("Large Text", True, WHITE)

# Get rectangles
text1_rect = text1_surface.get_rect(topleft=(50, 50))
text2_rect = text2_surface.get_rect(topright=(WIDTH - 50, 50))

# Blit texts
screen.blit(text1_surface, text1_rect)
screen.blit(text2_surface, text2_rect)
```
<br><br>

## Dynamic Text Variables
To display text that changes as the program runs, we'll re-render the text surface and blit it to the screen.

It's important to include the code to re-render the text surface inside the main game loop, since you want this to be updating constantly.

### Full Example
This [example](dynamic_text_example.py) displays a score that changes as the player mashes the space bar:

```python
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
```

Notice the text surface is re-rendered each game loop. We pull from the `score` variable, redefine the text string using [f-string formatting](https://fstring.help/), then re-render the text surface for blitting.