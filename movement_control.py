import coordinate_conversion as convert

def valid_piece(coord: str, player_number: int, board: iter) -> bool:
    """
    Checks whether the square specified by `coord` contains a valid piece for the player
    number provided. Player number must be a 1 or 2.
    """
    pieces = ['P', 'N', 'B', 'R', 'Q', 'K']

    row, column = convert.grid_coord_to_index(coord)
    piece: str = board[row][column]

    if piece.upper() not in pieces:
        return False
    if player_number == 1 and not piece.islower():
        return False
    if player_number == 2 and not piece.isupper():
        return False
    
    return True