import coordinate_conversion as convert
import numpy as np
from colours import Colours

class Chess():
    def __init__(self) -> None:

        self.board = np.array([
            ["-", "A", "B", "C", "D", "E", "F", "G", "H"],
            ['8', 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['7', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['6', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['5', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['4', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['3', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['2', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['1', 'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ])

        self.moves = []     # (moved_piece, taken_piece, current_coord, moved_coord)

    def reset_board(self) -> None:
        
        self.board = np.array([
            ["-", "A", "B", "C", "D", "E", "F", "G", "H"],
            ['8', 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['7', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['6', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['5', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['4', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['3', '0', '0', '0', '0', '0', '0', '0', '0'],
            ['2', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['1', 'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ])

    def print_control_guide() -> None:
        """
        Prints the control guide to the display terminal. Takes no arguemnts.
        """

        key = 'Key: R - Rook, N - Knight, B - Bishop, K - King, Q - Queen, P - Pawn.'

        print('Lowercase is player 1, uppercase is player 2, player 1 goes first.')
        print(key, end = '\n\n')
        print(Colours.BOLD + Colours.GREEN + "Control Guide" + Colours.ENDC)
        print("-------------")
        print("Choose the piece you wish to move when prompted, make sure the case type matches your player type.")
        print("Enter the square you wish to move that piece to.", end="\n\n")
        print("Other Commands:")
        print(Colours.BOLD + "CASTLE" + Colours.ENDC + " - when you wish to castle your king.")
        print(Colours.BOLD + "MOVES" + Colours.ENDC + " - prints a list of all previous moves.")
        print(Colours.BOLD + "PRINT" + Colours.ENDC + " - prints the current board to terminal.")
        print(Colours.BOLD + "GUIDE" + Colours.ENDC + " - prints the control guide to terminal.", end = "\n\n")

    def move_piece(self) -> None:
        pass

    def play(self) -> None:
        pass
    

    


if __name__ == "__main__":
    pass