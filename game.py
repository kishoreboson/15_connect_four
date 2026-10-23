
from board import Board
from ai import AI


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.turn = "X"

    def run(self):
        print("Connect Four — you are X.")

        while True:
            self.board.print()

            if self.turn == "X":
                raw = input("Column (1-7), or q: ").strip().lower()

                if raw == "q":
                    print("Game ended.")
                    return

                try:
                    col = int(raw) - 1
                except ValueError:
                    print("Enter a column number from 1 to 7.")
                    continue

                if not 0 <= col < 7:
                    print("Choose a column from 1 to 7.")
                    continue

            else:
                col = self.ai.choose_column(self.board)

            if col is None:
                self.board.print()
                if self.board.full():
                    print("Draw.")
                else:
                    print("AI could not find a legal move. Game ended.")
                return

            row = self.board.drop(col, self.turn)

            if row is None:
                if self.turn == "O":
                    print("AI selected an unavailable column. Game ended.")
                    return

                print("Column full. Choose another column.")
                continue

            # Feedback occurs once, after a successful placement.
            print(f"{self.turn} placed a disc in column {col + 1}.")

            # Check win before asking for another turn.
            if self.board.winner(self.turn):
                self.board.print()
                print(self.turn, "wins!")
                return

            if self.board.full():
                self.board.print()
                print("Draw.")
                return

            self.turn = "O" if self.turn == "X" else "X"
