import pygame
import queue


# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))

# Define the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

def createMaze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "X", "#"])

    return maze


def createMaze2():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "#", "#", "X", "#"])

    return maze


def createMaze3():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", "#", "#"])
    maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "#", "#", "X", "#"])

    return maze

def createMaze4():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", "#", "#"])
    maze.append(["#", " ", "#", "#", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", "#", "#", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "#", "#", "X", "#"])

    return maze

def createMaze5():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", "#", "#", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "X", "#"])

    return maze



# Convert the maze to a format that Pygame can understand
def to_pygame(maze):
    pygame_maze = []
    for row in maze:
        pygame_row = []
        for cell in row:
            if cell == "#":
                pygame_row.append(black)
            else:
                pygame_row.append(white)
        pygame_maze.append(pygame_row)
    return pygame_maze

# Draw the maze
def draw_maze(maze, screen, block_size=20):
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
            pygame.draw.rect(screen, cell, rect)

# Main game loop
def main_loop(screen, maze):
    clock = pygame.time.Clock()
    running = True

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the maze
        draw_maze(maze, screen)

        # Update the display
        pygame.display.update()

        # Limit the framerate
        clock.tick(30)

    pygame.quit()


def printMaze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print(color + "+ " + "\033[0m", end="")   # the color
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "#"):
            return False

    return True


def findEnd(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    i = start
    j = 0
    count = 0
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print("Found: " + moves)
        for i in moves:
            count += 1
        print("The Number of correct path to reach the end is: ", count)
        printMaze(maze, moves)
        return True
    return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # MAIN ALGORITHM
    color = "\033[92m"   # color for the path
    move_counter = 0     # counter of all the moves used in the algorithm
    nums = queue.Queue()
    nums.put("")
    add = ""
    # user can choose what king of maze
    print("Please select a maze:")
    print("1. Maze 1")   # maze 1
    print("2. Maze 2")   # maze 2
    print("3. Maze 3")   # maze 3
    print("4. Maze 4")   # maze 4
    print("5. Maze 5")   # maze 5
    selected_maze = int(input("Enter your choice: "))
    if selected_maze == 1:
        maze = createMaze()
    elif selected_maze == 2:
        maze = createMaze2()
    elif selected_maze == 3:
        maze = createMaze3()
    elif selected_maze == 4:
        maze = createMaze4()
    else:
        maze = createMaze5()

    while not findEnd(maze, add):
        add = nums.get()
        move_counter += 1  # counter all moves used in algorithm
        # print(add)
        for j in ["L", "R", "U", "D"]:
            put = add + j
            if valid(maze, put):
                nums.put(put)
    print("Number of steps used to solve the maze:", move_counter)

    # Convert the maze to a format that Pygame can understand
    pygame_maze = to_pygame(maze)

    # Start the main game loop
    main_loop(screen, pygame_maze)
    pygame.display.update()

# Quit Pygame
pygame.quit()
