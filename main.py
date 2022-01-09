from utils import *
import math

# Calculate dimensions of display and pixel size; create display
width = COLS * round(APPROX_WIDTH // COLS)
pixel_size = width // COLS

max_num_colors = get_longest_palette(palette_colors)[1]
toolbar_height = int(math.ceil(max_num_colors/COLOR_BUTTONS_PER_ROW) * COLOR_BUTTON_SIZE + 2*TOOLBAR_BUFFER_SIZE)

height = ROWS * pixel_size + toolbar_height

WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pixel Art Designer")


def init_grid(rows, cols, color):
    grid_to_draw = []
    for i in range(rows):
        grid_to_draw.append([])
        for _ in range(cols):
            grid_to_draw[i].append(color)
    return grid_to_draw


def make_color_buttons(colors, max_per_row):
    buttons = []
    for j, color in enumerate(colors):
        row = j // max_per_row
        buttons.append(Button(
            TOOLBAR_BUFFER_SIZE + (j - row * max_per_row) * COLOR_BUTTON_SIZE,  # x
            height - toolbar_height + TOOLBAR_BUFFER_SIZE + row * COLOR_BUTTON_SIZE,  # y
            COLOR_BUTTON_SIZE,  # width
            COLOR_BUTTON_SIZE,  # height
            pygame.Color(color)  # color
        ))
    return buttons


def draw_grid(win, grid_to_draw):
    for i, row in enumerate(grid_to_draw):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * pixel_size, i * pixel_size, pixel_size, pixel_size))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * pixel_size), (width, i * pixel_size))

        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * pixel_size, 0), (i * pixel_size, height - toolbar_height))


def draw(win, grid_to_draw, color_buttons_to_draw):
    win.fill(BG_COLOR)
    draw_grid(win, grid_to_draw)

    for button in color_buttons_to_draw:
        button.draw(win)

    pygame.display.update()


def get_pixel_from_pos(pos):
    x, y = pos
    row = y // pixel_size
    col = x // pixel_size

    if row >= ROWS:  # Raise error if the click is in the toolbar area
        raise IndexError

    return row, col


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

palette = 'NES'
color_buttons = make_color_buttons(palette_colors[palette], COLOR_BUTTONS_PER_ROW)

# Button(310, button_y, MENU_BUTTON_SIZE, MENU_BUTTON_SIZE, WHITE, "Clear", BLACK)

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
            pos = pygame.mouse.get_pos()

            try:
                row, col = get_pixel_from_pos(pos)
                grid[row][col] = drawing_color

            except IndexError:  # Means click was in the toolbar area
                for button in color_buttons:
                    button.selected = False

                    if button.clicked(pos):

                        if button.text == "Clear":
                            grid = init_grid(ROWS, COLS, BG_COLOR)
                            drawing_color = BLACK

                        else:
                            button.selected = True
                            drawing_color = button.color

    draw(WIN, grid, color_buttons)

pygame.quit()
