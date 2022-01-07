from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8-bit Designer")


def init_grid(rows, cols, color):
    grid_to_draw = []
    for i in range(rows):
        grid_to_draw.append([])
        for _ in range(cols):
            grid_to_draw[i].append(color)
    return grid_to_draw


def draw_grid(win, grid_to_draw):
    for i, row in enumerate(grid_to_draw):
        for j, pixel in enumerate(row):
            pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    if DRAW_GRID_LINES:
        for i in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))

        for i in range(COLS + 1):
            pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw(win, grid_to_draw, buttons):
    win.fill(BG_COLOR)
    draw_grid(win, grid_to_draw)

    for button in buttons:
        button.draw(win)

    pygame.display.update()


def get_pixel_from_pos(pos):
    x, y = pos
    row = y // PIXEL_SIZE
    col = x // PIXEL_SIZE

    if row >= ROWS:  # Raise error if the click is in the toolbar area
        raise IndexError

    return row, col


run = True
clock = pygame.time.Clock()
grid = init_grid(ROWS, COLS, BG_COLOR)
drawing_color = BLACK

button_y = HEIGHT - TOOLBAR_HEIGHT//2 - 25
buttons = [
    Button(10, button_y, 50, 50, BLACK),
    Button(70, button_y, 50, 50, RED),
    Button(130, button_y, 50, 50, GREEN),
    Button(190, button_y, 50, 50, BLUE),
    Button(250, button_y, 50, 50, WHITE),
    Button(310, button_y, 50, 50, WHITE, "Clear", BLACK)
]

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

            except IndexError:
                for button in buttons:
                    button.selected = False

                    if button.clicked(pos):
                        button.selected = True
                        drawing_color = button.color

                        if button.text == "Clear":
                            grid = init_grid(ROWS, COLS, BG_COLOR)
                            drawing_color = BLACK

    draw(WIN, grid, buttons)

pygame.quit()
