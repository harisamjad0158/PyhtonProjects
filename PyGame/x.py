import pygame
import sys
import numpy as np


pygame.init()

# Define window dimensions
WINDOW_SIZE = (300, 300)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tic Tac Toe")


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font
font = pygame.font.Font(None, 80)

# Initialize the game board as a 3x3 array
board = np.zeros((3, 3))


def draw_board():
    screen.fill(WHITE)

    # Draw grid lines
    for i in range(1, 3):
        pygame.draw.line(screen, BLACK, (i * 100, 0), (i * 100, 300), 3)
        pygame.draw.line(screen, BLACK, (0, i * 100), (300, i * 100), 3)

    # Draw X's and O's on the board
    for row in range(3):
        for col in range(3):
            if board[row, col] == 1:
                x_pos = col * 100 + 50
                y_pos = row * 100 + 50
                pygame.draw.line(screen, BLACK, (x_pos - 30, y_pos - 30), (x_pos + 30, y_pos + 30), 3)
                pygame.draw.line(screen, BLACK, (x_pos + 30, y_pos - 30), (x_pos - 30, y_pos + 30), 3)
            elif board[row, col] == 2:
                pygame.draw.circle(screen, BLACK, (col * 100 + 50, row * 100 + 50), 30, 3)

def check_winner(player):
    for row in range(3):
        if all(board[row, :] == player):
            return True

    for col in range(3):
        if all(board[:, col] == player):
            return True

    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
def main():
    current_player = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not check_winner(1) and not check_winner(2) and not check_draw():
                x, y = pygame.mouse.get_pos()
                row, col = y // 100, x // 100

                if board[row, col] == 0:
                    board[row, col] = current_player
                    current_player = 3 - current_player  # Switch between player 1 and player 2

        draw_board()
        pygame.display.update()

        if check_winner(1):
            print("Player 1 wins!")
            break
        elif check_winner(2):
            print("Player 2 wins!")
            break
        elif check_draw():
            print("It's a draw!")
            break


if __name__ == "__main__":
    main()

return False

def check_draw():
    return not any(0 in row for row in board)



