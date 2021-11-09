# Libraries
import pygame
from cell import Cell
from CONSTANTS import WIDTH, HEIGHT, SIZE, CELL_SIZE
from slider import Slider


# Init pygame components
pygame.init()

# Init the font for the text
font = pygame.font.Font("assets/fonts/FreeSansBold.ttf", 28)

# set a clock to fix the FPS
clock = pygame.time.Clock()

# Init window
screen = pygame.display.set_mode((SIZE[0], SIZE[1] + 200), pygame.RESIZABLE)
pygame.display.set_caption("Maze Generator")

# Init the rows and cols
rows, cols = int(WIDTH / CELL_SIZE), int(HEIGHT / CELL_SIZE)
# Init the grid which contains the cells
grid = []
# Init the stack for recursion
stack = []

# create all cells
for i in range(rows):
    for j in range(cols):
        grid.append(Cell(i, j))

# set the beginning of the maze to the upper left corner
current = grid[0]
# set the current cell as visited
current.visited = True


def removeWalls(a, b):
    """
    Remove walls of the cells a and b
    :param a: first cell
    :param b: second cell
    :return:
    """
    x = a.i - b.i
    if x == 1:
        a.walls[3] = False
        b.walls[1] = False
    elif x == -1:
        a.walls[1] = False
        b.walls[3] = False
    y = a.j - b.j
    if y == 1:
        a.walls[0] = False
        b.walls[2] = False
    elif y == -1:
        a.walls[2] = False
        b.walls[0] = False


# create a slider for the cell size
slider = Slider(WIDTH / 2 - 150, HEIGHT + 100 - 5, 300, 10, 10, (255, 255, 255), 50, (200, 200, 200))

running = True
while running:
    # fill the screen
    screen.fill((51, 51, 51))

    # display each cell
    for cell in grid:
        cell.show(screen)

    # get a random neighbor
    neighbor = current.checkNeighbors(grid)
    # if there is a neighbor available
    if neighbor is not None:
        # set the neighbor
        neighbor.visited = True
        # add this neighbor to the stack for recursion
        stack.append(current)
        # remove walls between current and neighbor
        removeWalls(current, neighbor)
        # set the current cell to the neighbor
        current = neighbor
    # if there are still cells in the stack
    elif len(stack):
        # unstack
        current = stack.pop()

    # draw slider and check it (for position and value)
    slider.draw(screen)
    slider.check()

    # change the size of the cell (update when redraw a maze)
    # the minimum size is 10 and maximum size is 90 (< 10 may slow down your computer, > 90 has only a few cells)
    cell_size = int(round(slider.value, 2) * 80) + 10
    # Display the size of the cell
    text = font.render("Cell size : " + str(cell_size), False, (255, 255, 255))
    screen.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT + 50 - text.get_height() / 2))

    # Fix FPS to 180
    clock.tick(180)
    # update window
    pygame.display.update()

    # get all events
    for event in pygame.event.get():
        # stop program
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # if mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            # on the maze
            if 0 < pygame.mouse.get_pos()[0] < WIDTH and 0 < pygame.mouse.get_pos()[1] < HEIGHT:
                # reset the maze and regenerate it
                rows, cols = int(WIDTH / cell_size), int(HEIGHT / cell_size)
                grid = []
                stack = []

                for i in range(rows):
                    for j in range(cols):
                        grid.append(Cell(i, j, cell_size))

                current = grid[0]
