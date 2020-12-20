# Your classic game of Tic-Tac-Toe
# Written by: Piero Orderique
# Date: 12/19/2020

from os import truncate


class TicTacToe:
    ROWS = 3
    COLS = 3

    def __init__(self, p1name = 'Piero', p2name = 'Fabrizzio') -> None:
        """P1 is X and P2 is O"""
        self.player1name = p1name
        self.player2name = p2name
        self.winner = ''
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
            # sepate with horizontal lines except for last row
            if row != self.ROWS-1:
                print('-'*3*self.COLS)

    def start_session(self):
        """call to start the game"""
        gameOver = False
        while not gameOver:
            self.winner = self.getWinner()
            # quit game if draw 
            if self.winner == 'Draw':
                gameOver = True
                print("\nGAME ENDED: DRAW")
                break
            #else keep playing the game
            # optionssss...
        self.show_winning_message(self.winner)

    def getWinner(self) -> str:
        """
        returns "None", P1.name, P2.name, or "DRAW" by checking winning conditions
        """
        full = True
        xCount = oCount = 0
        # check for empty cells AND row completions
        for row in self.board:
            for elem in row:
                if elem == ' ': full = False
                elif elem == 'X': xCount+=1
                elif elem == 'O': oCount+=1
            # reset the counters for next row
            xCount = oCount = 0 
        if full: return 'Draw'
        if xCount == 3: return self.player1name
        if oCount == 3: return self.player2name

        # now check for diagonals
        for idx1 in range(self.board):
            # TL to BR / TR to BL
            # [00] [11] [22] / [02] [11] [20]
            pass

    def show_winning_message(self, winnerName):
        """
        docstring
        """
        pass

    def __str__(self) -> str:
        board = ''
        for row in range(self.ROWS):
            board += (' | '.join(self.board[row])+'\n')
            if row != self.ROWS - 1:
                board += ('-'*3*self.COLS + '\n')
        return board



if __name__ == "__main__":
    print('\n'+'TIC-TAC-TOE GAME'.center(40, '='))
    # p1 = input('Player 1 Name: ')
    # p2 = input('Player 2 Name: ')
    GAME = TicTacToe()
    print(GAME)
