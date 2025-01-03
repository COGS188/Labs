import pygame
import sys

BOARD_SIZE = 8
SQUARE_SIZE = 75  # This sets the size of the chessboard squares
WINDOW_SIZE = BOARD_SIZE * SQUARE_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

pygame.init()

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('8 Queens Puzzle')

def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def place_queens(queen_positions):
    queen_image = pygame.image.load('queen.png')
    queen_image = pygame.transform.scale(queen_image, (SQUARE_SIZE, SQUARE_SIZE))
    for pos in queen_positions:
        screen.blit(queen_image, (pos[1] * SQUARE_SIZE, pos[0] * SQUARE_SIZE))

def is_safe(board, row, col):
    # TODO: Implement checks for whether it is safe to place a queen at board[row][col]
    # Hint: Consider horizontal, upper diagonal, and lower diagonal conflicts
    # Return True if it is safe to place a queen at board[row][col], otherwise return False

    return True  # Placeholder return

def solve_8_queens(board, col):
    # Base case: If all queens are placed
    if col >= BOARD_SIZE:
        return True

    # TODO: Iterate through each row in the current column to try placing the queen
    for i in ...:
        # TODO: Check if placing the queen at (i, col) is safe
        if ...:
            board[i][col] = 1  # Place this queen in board[i][col]

            if solve_8_queens(board, col + 1):
                return True
            
            # TODO: Backtrack: Remove queen from board[i][col]
            ...

    return False

def update_board():
    board = [[0]*BOARD_SIZE for _ in range(BOARD_SIZE)]
    if not solve_8_queens(board, 0):
        return []  # Return empty if no solution exists

    # Prepare the list of queen positions if a solution exists
    queen_positions = []
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == 1:
                queen_positions.append((i, j))

    return queen_positions

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board()
        queen_positions = update_board()  # Update the board with the new queen placements
        place_queens(queen_positions)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
