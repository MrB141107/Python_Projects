#pip install pygame

import sys
import pygame
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 25 #size of each grid cell

# Colors as defined by rgb values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
COLORS = [RED, BLUE, GREEN]

# Tetromino shapes - it represents the shapes of the tetris - "J", "L" , "I", "O", "S", "T", "Z". 
# The '0' represents a filled cell and '.' represents an empty cell within the Tetromino piece. 
# The pieces can be rotated and moved within the game grid. 
SHAPES = [
    [
        ['.....',
         '.....',
         '.....',
         'OOOO.',
         '.....'],
        ['.....',
         '..O..',
         '..O..',
         '..O..',
         '..O..']
    ],
    [
        ['.....',
         '.....',
         '..O..',
         '.OOO.',
         '.....'],
        ['.....',
         '..O..',
         '.OO..',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '..O..',
         '.....'],
        ['.....',
         '..O..',
         '..OO.',
         '..O..',
         '.....']
    ],
    [
        [
            '.....',
            '.....',
            '..OO.',
            '.OO..',
            '.....'],
        ['.....',
         '.....',
         '.OO..',
         '..OO.',
         '.....'],
        ['.....',
         '.O...',
         '.OO..',
         '..O..',
         '.....'],
        ['.....',
         '..O..',
         '.OO..',
         '.O...',
         '.....']
    ],
    [
        ['.....',
         '..O..',
         '..O.',
         '..OO.',
         '.....'],
        ['.....',
         '...O.',
         '.OOO.',
         '.....',
         '.....'],
        ['.....',
         '.OO..',
         '..O..',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '.O...',
         '.....']
    ],
]

#Tetromino class to represent individual pieces
class Tetromino:
    def __init__(self, x, y, shape):
        #Initialize tetromino properties
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(COLORS)  # You can choose different colors for each shape
        self.rotation = 0

#tetris class to manage the game
class Tetris:
    def __init__(self, width, height):
        #intitialize the tetris game
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.current_piece = self.new_piece() #Intitialize first tetromino
        self.game_over = False
        self.score = 0  # Keep track of the player's score

    def new_piece(self):
        # Choose a random shape
        shape = random.choice(SHAPES)
        # Return a new Tetromino object
        return Tetromino(self.width // 2, 0, shape)

    
    #Check if the current cell in the shape can be placed at a target position in the game grid
    #Try catch block is to handle potential IndexErrors that may occur if the target position is out of bounds.
    def valid_move(self, piece, x, y, rotation):
        """Check if the piece can move to the given position"""
        #Iterate over the cells of the Tetromino shape
        for i, row in enumerate(piece.shape[(piece.rotation + rotation) % len(piece.shape)]):
            for j, cell in enumerate(row):
                try:
                    if cell == 'O' and (self.grid[piece.y + i + y][piece.x + j + x] != 0):
                        return False
                except IndexError:
                    return False
        return True #valid if all cells in the Tetromino shape can be placed in the grid

    #Clear full lines in the game grid and return the number of lines cleared.
    def clear_lines(self):
        """Clear the lines that are full and return the number of cleared lines"""
        # Iterate through the rows in the game grid, excluding the last row.
        lines_cleared = 0
        for i, row in enumerate(self.grid[:-1]):
            if all(cell != 0 for cell in row):
                lines_cleared += 1
                del self.grid[i]
                self.grid.insert(0, [0 for _ in range(self.width)]) #insert a new line at the top to replace the cleared line.
        return lines_cleared


    #Lock the current piece in its current position and create a new piece to continue
    def lock_piece(self, piece):
        """Lock the piece in place and create a new piece"""
        # Iterate over the cells of the Tetromino piece's shape in its current rotation.
        for i, row in enumerate(piece.shape[piece.rotation % len(piece.shape)]):
            for j, cell in enumerate(row):
                if cell == 'O':
                    self.grid[piece.y + i][piece.x + j] = piece.color
        # Clear the lines and update the score
        lines_cleared = self.clear_lines()
        self.score += lines_cleared * 100  # Update the score based on the number of cleared lines
        # Create a new piece
        self.current_piece = self.new_piece()
        # Check if the game is over
        if not self.valid_move(self.current_piece, 0, 0, 0):
            self.game_over = True
        return lines_cleared #return number of lines cleared in this move.

    #Move current Tetromino piece down by one cell if game is not over.
    def update(self):
        """Move the tetromino down one cell"""
        if not self.game_over:
            if self.valid_move(self.current_piece, 0, 1, 0):
                self.current_piece.y += 1
            else:
                self.lock_piece(self.current_piece)

    #Draw game grid and the current Tetromino piece on the game screen.
    def draw(self, screen):
        """Draw the grid and the current piece"""
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:

                    #draw a rectangle representing the filled cell at appropriate position and size.
                    pygame.draw.rect(screen, cell, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1))

        #If there is current piece (game is not over), draw it on game screen.
        if self.current_piece:
            for i, row in enumerate(
                    self.current_piece.shape[self.current_piece.rotation % len(self.current_piece.shape)]):
                for j, cell in enumerate(row):
                    if cell == 'O':

                        #draw a rectangle representing the filled cell at appropriate position and size.
                        pygame.draw.rect(screen, self.current_piece.color, (
                        (self.current_piece.x + j) * GRID_SIZE, (self.current_piece.y + i) * GRID_SIZE, GRID_SIZE - 1,
                        GRID_SIZE - 1))

#Function to draw the score with the given font
def draw_score(screen, score, x, y):
    """Draw the score on the screen"""
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (x, y))

#Function to draw game over with the given font
def draw_game_over(screen, x, y):
    """Draw the game over text on the screen"""
    font = pygame.font.Font(None, 48)
    text = font.render("Game Over", True, RED)
    screen.blit(text, (x, y))

#Main function
def main():
    # Initialize pygame
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Tetris')
    # Create a clock object
    clock = pygame.time.Clock()
    # Create a Tetris object
    game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)
    fall_time = 0
    fall_speed = 50  #Adjust this value to change the falling speed, it's in milliseconds
    while True:
        # Fill the screen with black
        screen.fill(BLACK)
        for event in pygame.event.get():
            # Check for the QUIT event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Check for the KEYDOWN event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if game.valid_move(game.current_piece, -1, 0, 0):
                        game.current_piece.x -= 1  # Move the piece to the left
                if event.key == pygame.K_RIGHT:
                    if game.valid_move(game.current_piece, 1, 0, 0):
                        game.current_piece.x += 1  # Move the piece to the right
                if event.key == pygame.K_DOWN:
                    if game.valid_move(game.current_piece, 0, 1, 0):
                        game.current_piece.y += 1  # Move the piece down
                if event.key == pygame.K_UP:
                    if game.valid_move(game.current_piece, 0, 0, 1):
                        game.current_piece.rotation += 1  # Rotate the piece
                if event.key == pygame.K_SPACE:
                    while game.valid_move(game.current_piece, 0, 1, 0):
                        game.current_piece.y += 1  # Move the piece down until it hits the bottom
                    game.lock_piece(game.current_piece)  # Lock the piece in place
        # Get the number of milliseconds since the last frame
        delta_time = clock.get_rawtime()
        # Add the delta time to the fall time
        fall_time += delta_time
        if fall_time >= fall_speed:
            # Move the piece down
            game.update()
            # Reset the fall time
            fall_time = 0
        # Draw the score on the screen
        draw_score(screen, game.score, 10, 10)
        # Draw the grid and the current piece
        game.draw(screen)
        if game.game_over:
            # Draw the "Game Over" message
            draw_game_over(screen, WIDTH // 2 - 100, HEIGHT // 2 - 30)  # Draw the "Game Over" message
            # You can add a "Press any key to restart" message here
            # Check for the KEYDOWN event
            if event.type == pygame.KEYDOWN:
                # Create a new Tetris object
                game = Tetris(WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE)
        # Update the display
        pygame.display.flip()
        # Set the framerate
        clock.tick(60)

#Call main function to start the Tetris game when this script is executed.
if __name__ == "__main__":
    main()
