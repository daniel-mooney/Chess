import coordinate_conversion as convert

def valid_piece(coord: str, player_number: int, board: iter) -> bool:
    """
    Checks whether the square specified by `coord` contains a valid piece for the player
    number provided. Player number must be a 1 or 2.
    """
    pieces = ['P', 'N', 'B', 'R', 'Q', 'K']

    row, column = convert.grid_coord_to_index(coord)
    piece = board[row][column]

    if piece.upper() not in pieces:
        return False
    if player_number == 1 and not piece.islower():
        return False
    if player_number == 2 and not piece.isupper():
        return False
    
    return True

def valid_castle(castle_side: str, player: int, board: iter, moves: list) -> bool:
    pass

def valid_movement(start_coord: str, move_coord: str, board: iter) -> bool:
    """
    Checks if the movement made by the chosen piece fits that pieces movement contraints.
    Makes use of the alternative numeric coordinate system described in the README.
    """
    row, col = convert.grid_coord_to_index(start_coord)
    piece = board[row][col].upper()
    
    start_num = convert.grid_coord_to_num_coord(start_coord)
    move_num = convert.grid_coord_to_num_coord(move_coord)

    movement_functions = {'P': check_pawn_movement, 'N': check_knight_movement, 'B': check_bishop_movement,
                        'R': check_rook_movement, 'Q': check_queen_movement, 'K': check_king_movement}
    
    # Need to check for en pesant
    return movement_functions[piece](start_num, move_num, board)
   
# Movement Functions
def check_pawn_movement(start_num: int, move_num: int, board: iter) -> bool:
    """
    Checks if the movement defined by start_num to move_num is a valid movement direction for a pawn.
    """

    # Lowercase pawns are player 1, Uppercase is player 2
    i, j = convert.num_coord_to_index(start_num)
    player = 1 if board[i][j].islower() else 2
    direction = 1 if player == 1 else -1        # Travelling up or down the board, up is positive

    capture_movements = [9, 11]
    move_diff = (move_num - start_num) * direction

    if move_diff in capture_movements:
        m, n = convert.num_coord_to_index(move_num)
        capture_sq = board[m][n]

        return capture_sq != '0'
    
    # Check if pawn is being moved for the first time
    if player == 1:
        first_move = (start_num // 10) == 2
    else:
        first_move = (start_num // 10) == 7

    return move_diff == 10 or (first_move and move_diff == 20)

def check_knight_movement(start_num: int, move_num: int, board: iter) -> bool:
    """
    Checks if the movement defined by start_num to move_num is a valid movement direction for a knight.
    """
    valid_movements = [8, 12, 19, 21]
    move_diff = abs(move_num - start_num)

    return move_diff in valid_movements

def check_bishop_movement(start_num: int, move_num: int, board: iter) -> bool:
    """
    Checks if the movement defined by start_num to move_num is a valid movement direction for a bishop.
    """
    # Factors of 9 or 11 define diagonal movement
    valid_move_factors = [9, 11]
    move_diff = move_num - start_num

    if move_diff == 0:
        return False

    return any(move_diff % fac == 0 for fac in valid_move_factors) 

def check_rook_movement(start_num: int, move_num: int, board: iter) -> bool:
    """
    Checks if the movement defined by start_num to move_num is a valid movement direction for a rook.
    """
    # A move_diff of 10 represents movement up and down a file
    move_diff = abs(move_num - start_num)

    if move_diff == 0:
        return False

    return (move_diff % 10) == 0 or move_diff <= 7

def check_queen_movement(start_num: int, move_num: int, board: iter) -> bool:
    """
    Checks if the movement defined by start_num to move_num is a valid movement direction for a queen.
    """
    valid_move_factors = [9, 10, 11]
    move_diff = abs(move_num - start_num)

    if move_diff == 0:
        return False
    
    return any(move_diff % fac == 0 for fac in valid_move_factors) or move_diff <= 7

def check_king_movement(start_num: int, move_num: int, board: iter) -> bool:
    valid_move = [1, 9, 10, 11]
    move_diff = abs(move_num - start_num)

    return move_diff in valid_move


def valid_path(start_coord: str, move_coord: str, board: iter) -> bool:
    pass
