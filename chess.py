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

        print("The board as been reset")

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
        print("When prompted to chose a piece to move, you may enter any one of the commands below instead...", end = "\n\n")
        print("Commands:")
        print(Colours.BOLD + "CASTLE" + Colours.ENDC + " - when you wish to castle your king.")
        print(Colours.BOLD + "MOVES" + Colours.ENDC + " - prints a list of all previous moves.")
        print(Colours.BOLD + "BOARD" + Colours.ENDC + " - prints the current board to terminal.")
        print(Colours.BOLD + "GUIDE" + Colours.ENDC + " - prints the control guide to terminal.", end = "\n\n")
    
    def print_moves(self) -> None:
        pass

    def print_board(self) -> None:
        print(self.board, end = "\n\n")

    def move_piece(self) -> None:
        pass

    def play(self) -> None:
        """
        Runs a game of chess in the terminal.
        """
        commands = {"MOVES": self.print_moves, "BOARD": self.print_board,
                    "GUIDE": Chess.print_control_guide}
        player_number = 1

        Chess.print_control_guide()

        while True:
            break
    
    


if __name__ == "__main__":
    Chess.print_control_guide()