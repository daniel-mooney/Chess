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
    pass

def knight_movement(start_num: int, move_num: int, board: iter) -> bool:
    pass

def bishop_movement(start_num: int, move_num: int, board: iter) -> bool:
    pass

def rook_movement(start_num: int, move_num: int, board: iter) -> bool:
    pass

def queen_movement(start_num: int, move_num: int, board: iter) -> bool:
    pass

def king_movement(start_num: int, move_num: int, board: iter) -> bool:
    pass

