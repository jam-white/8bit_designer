import pygame
pygame.init()
pygame.font.init()

# Set RBG colours
WHITE = (255, 255, 255)
BLACK = pygame.Color("#000000")
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
GOLD = (255, 215, 7)

# Other settings
FPS = 60
APPROX_WIDTH, APPROX_HEIGHT = 700, 800
ROWS = COLS = 16
TOOLBAR_HEIGHT = APPROX_HEIGHT - APPROX_WIDTH
BG_COLOR = WHITE
BUTTON_FONT_SIZE = 16
BUTTON_SELECTED_BORDER_WIDTH = 6
DRAW_GRID_LINES = True


def get_font(size):
    return pygame.font.SysFont("arial", size)
