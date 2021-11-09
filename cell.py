# Libraries
import pygame
import random
from CONSTANTS import CELL_SIZE, HEIGHT, WIDTH


class Cell:
    def __init__(self, i, j, cell_size=CELL_SIZE):
        """
        Constructor of the cell
        :param i: position x of the cell
        :param j: position y of the cell
        :param cell_size: size of the cell
        """
        self.i = i
        self.j = j
        self.cell_size = cell_size
        # walls of the cells (True -> wall, False -> no wall)
        self.walls = [True, True, True, True]
        # if the cell has been visited
        self.visited = False

    def checkNeighbors(self, grid):
        """
        Check all neighbors of the cell
        :param grid: grid that contains all cells
        :return: None or list of neighbors who have not been visited
        """
        neighbors = []
        # 4 neighbors of the cell
        top = grid[index(self.i, self.j - 1, self.cell_size)] if index(self.i, self.j - 1,
                                                                       self.cell_size) != -1 else None
        right = grid[index(self.i + 1, self.j, self.cell_size)] if index(self.i + 1, self.j,
                                                                         self.cell_size) != -1 else None
        bottom = grid[index(self.i, self.j + 1, self.cell_size)] if index(self.i, self.j + 1,
                                                                          self.cell_size) != -1 else None
        left = grid[index(self.i - 1, self.j, self.cell_size)] if index(self.i - 1, self.j,
                                                                        self.cell_size) != -1 else None

        # check if each cell isn't None and visited
        if top is not None and not top.visited:
            neighbors.append(top)

        if right is not None and not right.visited:
            neighbors.append(right)

        if bottom is not None and not bottom.visited:
            neighbors.append(bottom)

        if left is not None and not left.visited:
            neighbors.append(left)

        # if there is at least one neighbor
        if len(neighbors) > 0:
            # return a random neighbors
            return neighbors[random.randint(0, len(neighbors) - 1)]
        else:
            return None

    def show(self, screen):
        """
        Display the cell on screen
        :param screen: pygame.Surface object, surface to display
        :return:
        """
        # if the cell is visited, display it in pink
        if self.visited:
            pygame.draw.rect(screen, (0, 0, 0),
                             (self.i * self.cell_size, self.j * self.cell_size, self.cell_size, self.cell_size))

        # draw a line if there is a wall
        if self.walls[0]:
            pygame.draw.line(screen, (255, 255, 255), (self.i * self.cell_size, self.j * self.cell_size),
                             (self.i * self.cell_size + self.cell_size, self.j * self.cell_size), 5)
        if self.walls[1]:
            pygame.draw.line(screen, (255, 255, 255),
                             (self.i * self.cell_size + self.cell_size, self.j * self.cell_size),
                             (self.i * self.cell_size + self.cell_size, self.j * self.cell_size + self.cell_size), 5)
        if self.walls[2]:
            pygame.draw.line(screen, (255, 255, 255),
                             (self.i * self.cell_size + self.cell_size, self.j * self.cell_size + self.cell_size),
                             (self.i * self.cell_size, self.j * self.cell_size + self.cell_size), 5)
        if self.walls[3]:
            pygame.draw.line(screen, (255, 255, 255),
                             (self.i * self.cell_size, self.j * self.cell_size + self.cell_size),
                             (self.i * self.cell_size, self.j * self.cell_size), 5)


def index(i, j, cell_size):
    """
    Return index of the cell
    :param i: position x of the cell
    :param j: position y of the cell
    :param cell_size: cell size
    :return: index of the cell or -1
    """
    if i < 0 or j < 0 or i > int(HEIGHT / cell_size) - 1 or j > int(WIDTH / cell_size) - 1:
        return -1
    return j + i * int(HEIGHT / cell_size)
