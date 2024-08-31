import pygame
import sys
from pygame import *

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Virtual Calculator")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

# Define fonts
small_font = pygame.font.Font(None, 30)
large_font = pygame.font.Font(None, 50)

# Define buttons
buttons = [
    ("7", 50, 200, 50, 50),
    ("8", 120, 200, 50, 50),
    ("9", 190, 200, 50, 50),
    ("/", 260, 200, 50, 50),
    ("4", 50, 270, 50, 50),
    ("5", 120, 270, 50, 50),
    ("6", 190, 270, 50, 50),
    ("*", 260, 270, 50, 50),
    ("1", 50, 340, 50, 50),
    ("2", 120, 340, 50, 50),
    ("3", 190, 340, 50, 50),
    ("-", 260, 340, 50, 50),
    ("C", 50, 410, 50, 50),
    ("0", 120, 410, 50, 50),
    ("=", 190, 410, 50, 50),
    ("+", 260, 410, 50, 50),
]

# Main loop
running = True
result = ""
while running:
    screen.fill(black)

    # Draw buttons
    for button in buttons:
        pygame.draw.rect(screen, gray, button[1:])
        text = small_font.render(button[0], True, white)
        text_rect = text.get_rect(center=(button[1] + button[3] // 2, button[2] + button[4] // 2))
        screen.blit(text, text_rect)

    # Draw result
    result_text = large_font.render(result, True, white)
    result_rect = result_text.get_rect(center=(200, 100))
    screen.blit(result_text, result_rect)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            x, y = event.pos
            for button in buttons:
                if x >= button[1] and x <= button[1] + button[3] and y >= button[2] and y <= button[2] + button[4]:
                    if button[0] == "=":
                        try:
                            result = str(eval(result))
                        except:
                            result = "Error"
                    elif button[0] == "C":
                        result = ""
                    else:
                        result += button[0]