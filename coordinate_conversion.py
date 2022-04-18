def grid_coord_to_num_coord(coord: str) -> int:
    """
    Converts a grid co-ordinate into a numeric co-ordinate used to control movement
    """
    coord = coord.upper()

    column = ord(coord[0]) - 64
    row = int(coord[1])

    return (row * 10) + column

def grid_coord_to_index(coord: str) -> tuple[int, int]:
    """
    Returns a tuple `(row, column)` for a given coordinate in the board matrix
    """
    row_index = [8 ,7, 6, 5, 4, 3, 2, 1]
    coord = coord.upper()

    row = row_index[int(coord[1]) - 1]
    column = ord(coord[0]) - 64

    return (row, column)

def num_coord_to_index(num_coord: int) -> tuple[int, int]:
    """
    Converts a num_coord to the corresponding row and column matrix coordinates.
    """
    
    row_index = [8 ,7, 6, 5, 4, 3, 2, 1]

    row = row_index[(num_coord // 10) - 1]
    column = num_coord % 10

    return (row, column)

def index_to_num_coord(row: int, column: int) -> int:
    """
    Converts a row, column pair into the corresponding num_coord used for movement control.
    """
    row_num = [80, 70, 60, 50, 40, 30, 20, 10]

    return row_num[row - 1] + column

def valid_coord(coord: str) -> bool:
    """
    Checks whether a chess grid co-ordinate is valid or not. Assumes the coordinate has been
    capitalised.
    """
    if len(coord) != 2:
        return False
    if coord[0] < 'A' or coord[0] > 'H':
        return False
    if coord[1] < '1' or coord[1] > '8':
        return False    

    return True