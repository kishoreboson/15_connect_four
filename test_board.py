
from board import Board
from ai import AI


def test_board_win(name, positions, expected):
    board = Board()

    for r, c in positions:
        board.grid[r][c] = "X"

    result = board.winner("X")
    assert result == expected, (
        f"{name}: expected {expected}, got {result}"
    )
    print(f"PASS: {name}")


def test_ai():
    ai = AI()

    # AI should win by placing O in column 4.
    board = Board()
    for c in range(3):
        board.grid[5][c] = "O"

    before = [row[:] for row in board.grid]
    move = ai.choose_column(board)
    assert move == 3, f"AI winning move expected 4, got {move + 1}"
    assert board.grid == before, "AI changed the board while analysing"
    print("PASS: AI takes immediate winning move")

    # AI should block X from winning in column 4.
    board = Board()
    for c in range(3):
        board.grid[5][c] = "X"

    before = [row[:] for row in board.grid]
    move = ai.choose_column(board)
    assert move == 3, f"AI blocking move expected 4, got {move + 1}"
    assert board.grid == before, "AI changed the board while analysing"
    print("PASS: AI blocks immediate player win")

    # A full board must not produce a move.
    board = Board()
    for r in range(6):
        for c in range(7):
            board.grid[r][c] = "X"

    assert ai.choose_column(board) is None
    print("PASS: AI handles a board with no legal moves")


def main():
    test_board_win(
        "Horizontal win",
        [(5, 0), (5, 1), (5, 2), (5, 3)],
        True,
    )
    test_board_win(
        "Vertical win",
        [(2, 0), (3, 0), (4, 0), (5, 0)],
        True,
    )
    test_board_win(
        "Diagonal down-right win",
        [(1, 0), (2, 1), (3, 2), (4, 3)],
        True,
    )
    test_board_win(
        "Diagonal down-left win",
        [(1, 3), (2, 2), (3, 1), (4, 0)],
        True,
    )
    test_board_win(
        "Three in a row is not a win",
        [(5, 0), (5, 1), (5, 2)],
        False,
    )

    board = Board()
    for r in range(6):
        board.grid[r][0] = "X"

    assert board.drop(0, "O") is None
    print("PASS: Full column rejects another disc")

    assert board.drop(-1, "O") is None
    assert board.drop(7, "O") is None
    print("PASS: Out-of-range columns are rejected")

    test_ai()
    print("\nAll automated tests passed!")


if __name__ == "__main__":
    main()
