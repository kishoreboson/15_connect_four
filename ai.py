
class AI:
    def choose_column(self, board, me="O", opponent="X"):
        legal = [
            c for c in range(7)
            if board.grid[0][c] == "."
        ]

        if not legal:
            return None

        # First: take an immediate winning move.
        for col in legal:
            row = board.drop(col, me)

            if row is not None:
                wins = board.winner(me)
                board.grid[row][col] = "."

                if wins:
                    return col

        # Second: block an immediate opponent win.
        for col in legal:
            row = board.drop(col, opponent)

            if row is not None:
                opponent_wins = board.winner(opponent)
                board.grid[row][col] = "."

                if opponent_wins:
                    return col

        # Otherwise: prefer the centre, then nearby columns.
        return min(legal, key=lambda c: abs(c - 3))
