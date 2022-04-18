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

    movement_functions = {'P': pawn_movement, 'N': knight_movement, 'B': bishop_movement,
                        'R': rook_movement, 'Q': queen_movement, 'K': king_movement}
    
    return movement_functions[piece](start_num, move_num, board)
   
# Movement Functions
def pawn_movement(start_num: int, move_num: int, board: iter) -> bool:
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

def knight_movement(start_num: int, move_num: int, board: iter) -> bool:
    valid_movements = [8, 12, 19, 21]
    move_diff = abs(move_num - start_num)

    return move_diff in valid_movements

def bishop_movement(start_num: int, move_num: int, board: iter) -> bool:
    # Factors of 9 or 11 define diagonal movement
    valid_move_factors = [9, 11]
    move_diff = move_num - start_num

    return any(move_diff % fac == 0 for fac in valid_move_factors) 

def rook_movement(start_num: int, move_num: int, board: iter) -> bool:
    pass

def queen_movement(start_num: int, move_num: int, board: iter) -> bool:
    pass

def king_movement(start_num: int, move_num: int, board: iter) -> bool:
    pass

