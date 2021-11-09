# Libraries
import pygame


class Slider:
    def __init__(self, x, y, w, h, radius, color, default_value, slider_color):
        """
        Constructor
        :param x: position x (top left corner of the slider)
        :param y: position y (top left corner of the slider)
        :param w: width
        :param h: height
        :param radius: border radius
        :param color: color o the slider
        :param default_value: default value of the slider
        :param slider_color: slider color
        """
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.radius = radius
        self.color = color
        self.default_value = default_value
        self.slider_color = slider_color
        # position and size of the cursor
        self.slider_x = (self.default_value / 100) * self.w + self.x
        self.slider_y = self.y
        self.slider_w = 15
        self.slider_h = 40
        # current value
        self.value = default_value / 100

    def draw(self, screen):
        """
        Display the slider on screen
        :param screen: pygame.Surface object, surface to display
        :return:
        """
        # base of the rect
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.w, self.h), border_radius=self.radius)
        # cursor
        pygame.draw.rect(screen, self.slider_color, (self.slider_x - self.slider_w / 2, self.slider_y - self.slider_h / 2 + self.h / 2, self.slider_w, self.slider_h), border_radius=15)

    def check(self):
        """
        Change the position of the slider and update the value
        :return:
        """
        # position of the mouse
        pos = pygame.mouse.get_pos()
        # check if the mouse is on the slider (+/- 15 for an offset if the motion of the mouse is high)
        if self.slider_x - 15 < pos[0] < self.slider_x + self.slider_w + 15 and self.slider_y - 15 < pos[1] < self.slider_y + self.slider_h + 15:
            # check if the left click mouse is pressed
            if pygame.mouse.get_pressed(3)[0]:
                # constrain the future position of the slider
                if self.x < pos[0] < self.x + self.w:
                    # Change position of the cursor
                    self.slider_x = pos[0]
                    # change slider value
                    offset = -1 if self.slider_x - self.x == 1 else 1
                    self.value = (self.slider_x - self.x + offset) / self.w
                else:
                    # set cursor position to the edges of the slider
                    self.slider_x = min([self.x, self.x + self.w], key=lambda x: abs(x - pos[0]))
