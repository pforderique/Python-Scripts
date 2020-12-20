# Your classic game of Tic-Tac-Toe
# Written by: Piero Orderique
# Date: 12/19/2020

class TicTacToe:
    ROWS = 3
    COLS = 3

    def __init__(self, p1name = 'Piero', p2name = 'Fabrizzio') -> None:
        self.player1name = p1name
        self.player2name = p2name
        self.create_board()

    def create_board(self, rows=ROWS, cols=COLS):
        """creates the row*col tic tac toe grid"""
        self.board = [[' ']*cols]
        for i in range(rows-1):
            self.board.append([' ']*cols)

    def print_board(self):
        for row in range(self.ROWS):
            showrow = ' | '.join(self.board[row])
            print(showrow)

    def start_session(self):
        """call to start the game"""
        

    def __str__(self) -> str:
        board = ''
        for row in range(self.ROWS):
            board += (' | '.join(self.board[row])+'\n')
        return board



if __name__ == "__main__":
    print('\n'*3)
    print('TIC-TAC-TOE GAME'.center(40, '='))
    # p1 = input('Player 1 Name: ')
    # p2 = input('Player 2 Name: ')
    GAME = TicTacToe()
    print(GAME)
