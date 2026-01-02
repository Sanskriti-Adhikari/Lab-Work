class Game:
    def __init__(self):  # Constructor
        self.reset()

    def reset(self):  # Defaults for a new game
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = ' '

    def draw_board(self):
        print()
        for i in range(3):
            print(" | ".join(self.board[i]))
            if i < 2:
                print("--+---+--")
        print()

    def check_winner(self):
        for i in range(3):
            # Rows checking
            if self.board[i][0] != ' ' and \
               self.board[i][0] == self.board[i][1] and \
               self.board[i][1] == self.board[i][2]:
                self.winner = self.board[i][0]
                self.game_over = True
                return

            # Columns checking
            if self.board[0][i] != ' ' and \
               self.board[0][i] == self.board[1][i] and \
               self.board[1][i] == self.board[2][i]:
                self.winner = self.board[0][i]
                self.game_over = True
                return

        # Diagonal checking
        if self.board[0][0] != ' ' and \
           self.board[0][0] == self.board[1][1] and \
           self.board[1][1] == self.board[2][2]:
            self.winner = self.board[0][0]
            self.game_over = True
            return

        if self.board[0][2] != ' ' and \
           self.board[0][2] == self.board[1][1] and \
           self.board[1][1] == self.board[2][0]:
            self.winner = self.board[0][2]
            self.game_over = True
            return

        # Checking for draw
        full = True
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    full = False

        if full:
            self.winner = ' '
            self.game_over = True

    def handle_input(self):
        if self.game_over:
            if self.winner == ' ':
                print("Draw!")
            else:
                print(self.winner, "wins!")
            input("Press Enter to restart...")
            self.reset()
            return

        print(self.current_player, "'s turn")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if row >= 0 and row < 3 and col >= 0 and col < 3:
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                self.check_winner()

                if not self.game_over:
                    if self.current_player == 'X':
                        self.current_player = 'O'
                    else:
                        self.current_player = 'X'
            else:
                print("Cell already occupied.")
        else:
            print("Invalid position.")

    def update_and_draw(self):
        self.draw_board()
        self.handle_input()


def main():
    game = Game()
    while True:
        game.update_and_draw()

main()