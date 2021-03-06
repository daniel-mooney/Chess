import movement_control as ctrl
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

        self.moves = []

        print("The game has been reset!", end="\n\n")

    def print_control_guide() -> None:
        """
        Prints the control guide to the display terminal. Takes no arguemnts.
        """

        key = 'Key: R - Rook, N - Knight, B - Bishop, K - King, Q - Queen, P - Pawn.'

        print('\nLowercase is player 1, uppercase is player 2, player 1 goes first.')
        print(key, end='\n\n')
        print(Colours.BOLD + Colours.GREEN + "Control Guide" + Colours.ENDC)
        print("-------------")
        print("Choose the piece you wish to move when prompted, make sure the case type matches your player type.")
        print("Enter the square you wish to move that piece to.", end="\n\n")
        print("When prompted to chose a piece to move, you may enter any one of the commands below instead...", end="\n\n")
        print("Commands:")
        print(Colours.BOLD + "CASTLE" + Colours.ENDC + " - when you wish to castle your king.")
        print(Colours.BOLD + "MOVES" + Colours.ENDC + " - prints a list of all previous moves.")
        print(Colours.BOLD + "QUIT" + Colours.ENDC + " - ends the current game and closes the program.")
        print(Colours.BOLD + "RESET" + Colours.ENDC + " - resets the current game being played.")
        print(Colours.BOLD + "GUIDE" + Colours.ENDC + " - prints the control guide to terminal.", end="\n\n")
    
    def print_moves(self) -> None:
        pass

    def print_board(self) -> None:
        print(f"\n{self.board}", end="\n\n")

    def move_piece(self, start_coord: str, move_coord: str, player: int) -> bool:
        """
        Moves a piece in the current instance's `self.board` variable. Updates the moves list.
        Contains error checking for move inputs. Returns `True` if piece successfully moved
        else `False`.
        """
        row, col = convert.grid_coord_to_index(start_coord)
        if not ctrl.valid_piece(start_coord, player, self.board):
            print(Colours.FAIL + Colours.BOLD + f"\nInvalid piece selection at {start_coord}: {self.board[row][col]}" + Colours.ENDC)
            return False
        
        if not ctrl.valid_movement(start_coord, move_coord, self.board):
            print(Colours.FAIL + Colours.BOLD + f"\nCannot move {self.board[row][col]}({start_coord}) to {move_coord}" + Colours.ENDC)
            return False

        return True


        # Valid movement
        # valid path
        # piece not pinned
        

    def play(self) -> None:
        """
        Runs a game of chess in the terminal.
        """
        # CASTLE is a special movement related command and hence is not included in the command dictionary,
        # instead being handled with the rest of movements
        commands = {"MOVES": self.print_moves, "GUIDE": Chess.print_control_guide,
                    "RESET": self.reset_board, "QUIT": None}

        player_number = 1
        Chess.print_control_guide()
        input("Press [ENTER] to begin...")

        while True:
            self.print_board()

            start_coord = input("Chose a piece to move: ")
            start_coord = start_coord.upper()            

            if start_coord in commands:
                if start_coord == "QUIT":
                    print("Exiting game...")
                    break

                commands[start_coord]()
                input("Press [ENTER] to continue...")
                continue

            if start_coord == "CASTLE":
                move_coord = input("King (K) or Queen (Q) side: ")
                move_coord = move_coord.upper()

                if move_coord != 'K' and move_coord != 'Q':
                    print(Colours.FAIL + Colours.BOLD + f"\nInvalid CASTLE command: {move_coord}" + Colours.ENDC)
                    print(f"Player {player_number} please try again.", end="\n\n")
                    input("Press [ENTER] to continue...")
                    continue

            else:
                if not convert.valid_coord(start_coord):
                    print(Colours.FAIL + Colours.BOLD + f"\nInvalid start co-ordinate: {start_coord}" + Colours.ENDC)
                    print(f"Player {player_number} please try again.", end="\n\n")
                    input("Press [ENTER] to continue...")
                    continue

                move_coord = input("Move piece where: ")
                move_coord = move_coord.upper()

                if not convert.valid_coord(move_coord):
                    print(Colours.FAIL + Colours.BOLD + f"\nInvalid move co-ordinate: {move_coord}" + Colours.ENDC)
                    print(f"Player {player_number} please try again.", end="\n\n")
                    input("Press [ENTER] to continue...")
                    continue
            
            valid_move = self.move_piece(start_coord, move_coord, player_number)

            if valid_move:
                player_number = 2 if player_number == 1 else 1
            else:
                print(f"Player {player_number} please try again.", end="\n\n")
                input("Press [ENTER] to continue...")

             
    
def main():
    game = Chess()
    game.play()

if __name__ == "__main__":
    main()