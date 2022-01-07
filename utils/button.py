from .settings import *


class Button:
    def __init__(self, x, y, width, height, color, text=None, text_color=BLACK, selected=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.selected = selected

    def create_selected_frame(self, win):
        """Creates frame showing which button is selected"""
        pygame.draw.rect(win, BLACK, (self.x, self.y, self.width, self.height), BUTTON_SELECTED_BORDER_WIDTH)
        # Top triangle
        pygame.draw.polygon(win, GOLD, [(self.x + 2 * self.width // 5, self.y),
                                        (self.x + 3 * self.width // 5, self.y),
                                        (self.x + self.width // 2, self.y + BUTTON_SELECTED_BORDER_WIDTH)])
        # Left triangle
        pygame.draw.polygon(win, GOLD, [(self.x, self.y + 2 * self.height // 5),
                                        (self.x, self.y + 3 * self.height // 5),
                                        (self.x + BUTTON_SELECTED_BORDER_WIDTH, self.y + self.height // 2)])
        # Right triangle
        pygame.draw.polygon(win, GOLD, [(self.x + self.width, self.y + 2 * self.height // 5),
                                        (self.x + self.width, self.y + 3 * self.height // 5),
                                        (self.x + self.width - BUTTON_SELECTED_BORDER_WIDTH,
                                         self.y + self.height // 2)])
        # Bottom triangle
        pygame.draw.polygon(win, GOLD, [(self.x + 2 * self.width // 5, self.y + self.height),
                                        (self.x + 3 * self.width // 5, self.y + self.height),
                                        (self.x + self.width // 2, self.y + self.height -
                                         BUTTON_SELECTED_BORDER_WIDTH)])

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, BLACK, (self.x, self.y, self.width, self.height), 1)

        if self.text:
            button_font = get_font(BUTTON_FONT_SIZE)
            text_surface = button_font.render(self.text, True, self.text_color)
            win.blit(text_surface, (self.x + self.width//2 - text_surface.get_width()//2,
                                    self.y + self.height//2 - text_surface.get_height()//2))

        if self.selected:
            self.create_selected_frame(win)

    def clicked(self, pos):
        x, y = pos

        if not self.x <= x <= self.x + self.width:
            return False
        if not self.y <= y <= self.y + self.height:
            return False

        return True
