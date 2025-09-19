# This is a program that validates if a chess board is a valid chess board


def checkChessBoard(board):
    # Define the set of all chess pieces
    # Define the pieces and colors
    pieces = ["king", "queen", "rook", "knight", "bishop", "pawn"]
    colors = ["b", "w"]

    # Set of all chess pieces
    all_pieces = set(color + piece for piece in pieces for color in colors)

    # Define the valid count range of pieces
    valid_counts = {
        "king": (1, 1),
        "queen": (0, 1),
        "rook": (0, 2),
        "knight": (0, 2),
        "bishop": (0, 2),
        "pawn": (0, 8),
    }

    # Count all the pieces on the board
    piece_count = {}
    for v in board.values():
        if v in all_pieces:
            piece_count.setdefault(v, 0)
            piece_count[v] += 1

    # Check pieces count in valid range
    for piece in all_pieces:
        count = piece_count.get(piece, 0)
        lo, hi = valid_counts[piece[1:]]
        if not lo <= count <= hi:  # Count needs to be between lo and hi
            if lo != hi:
                print(
                    f"There should be between {lo} and {hi} {piece} but there are {count}."
                )
            else:
                print(f"There should be {lo} {piece} but there are {count}.")
            return False

    # Check that positions are valid
    for location in board.keys():
        row = int(location[:1])
        column = location[1:]
        if not ((1 <= row <= 8) and ("a" <= column <= "h")):
            print(f"Invalid to have {board[location]} at position {location}.")
            return False

    # Check that pieces names are valid
    for loc, piece in board.items():
        if piece:
            if piece not in all_pieces:
                print(f"{piece} is not a valid chess piece at position {loc}.")
                return False

    return True
