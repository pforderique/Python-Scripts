# Your classic game of Tic-Tac-Toe
# Written by: Piero Orderique
# Date: 12/19/2020

class TicTacToe:
    SIZE = 3
    ROWS = COLS = SIZE

    def __init__(self, p1name = 'Piero', p2name = 'Fabrizzio') -> None:
        """P1 is X and P2 is O"""
        self.player1name = p1name
        self.player2name = p2name
        self.winner = ''
        self.round = 1
        self.gameOver = False
        self.options = {'TL':(0,0), 'TC':(0,1), 'TR':(0,2), 'CL':(1,0), 'CC':(1,1),
                        'CR':(1,2), 'BL':(2,0), 'BC':(2,1), 'BR':(2,2)}
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
        while not self.gameOver:
            self.winner = self.getWinner()
            # quit game if draw or winner found
            self.check_termination()
            if self.gameOver: break
            # else keep playing the game - player 1
            self.prompt(self.player1name)
            self.winner = self.getWinner()
            self.check_termination()
            if self.gameOver: break
            # player 2
            self.prompt(self.player2name)
            self.winner = self.getWinner()
            self.check_termination()
            if self.gameOver: break
            # increment round number 
            self.round += 1
        
    def prompt(self, playerName):
        """prompts choices for player"""
        print("ROUND {}: {}'s turn".format(self.round, playerName).center(40,'-')+'\n')
        self.print_board()
        choice = input("""Choose where to mark from the following options: \n""" + str(self.options.keys()) +'\n')
        while choice not in self.options:
            choice = input("""Invalid option. Choose where to mark from the following options: \n""" + str(self.options.keys()) +'\n')
        # get thoose coordinates and remove from options
        row = self.options[choice][0]
        col = self.options[choice][1]
        del self.options[choice]
        # place an X in that location if player X
        if playerName == self.player1name:
            self.board[row][col] = 'X'
        elif playerName == self.player2name:
            self.board[row][col] = 'O'        

    def check_termination(self):
        """check if termination can occur and sets gameOver"""
        if self.winner == 'Draw':
            self.gameOver = True
            print("\nGAME ENDED: DRAW")
        elif self.winner == self.player1name or self.winner == self.player2name:
            self.gameOver = True
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
            if xCount == self.SIZE: return self.player1name
            if oCount == self.SIZE: return self.player2name
            # else reset the counters for next row
            xCount = oCount = 0 

        # check columns
        xCount = oCount = 0
        for col in range(self.SIZE):
            for row in range(self.SIZE):
                if self.board[row][col] == 'X': xCount+=1
                elif self.board[row][col] == 'O': oCount+=1
            if xCount == self.SIZE: return self.player1name
            if oCount == self.SIZE: return self.player2name
            # else reset the counters for next col
            xCount = oCount = 0 

        # check for TL to BR diagonal
        xCount = oCount = 0
        for idx in range(self.SIZE):
            if self.board[idx][idx] == 'X': xCount+=1
            elif self.board[idx][idx] == 'O': oCount+=1
        if xCount == self.SIZE: return self.player1name
        if oCount == self.SIZE: return self.player2name
            
        # check for TR to BL diagonal
        xCount = oCount = 0
        for idx in range(self.SIZE):
            if self.board[idx][self.SIZE - 1 - idx] == 'X': xCount+=1
            elif self.board[idx][self.SIZE - 1 - idx] == 'O': oCount+=1
        if xCount == self.SIZE: return self.player1name
        if oCount == self.SIZE: return self.player2name

        # if none of the above return an asnwer but board is full: DRAW
        if full: return 'Draw'
         
        return "None"
            
    def show_winning_message(self, winnerName):
        """prints congratulatory message"""
        self.print_board()
        print("GAME ENDED: {} WINS!".format(winnerName).center(40, '*'))

    def __str__(self) -> str:
        board = ''
        for row in range(self.ROWS):
            board += (' | '.join(self.board[row])+'\n')
            if row != self.ROWS - 1:
                board += ('-'*3*self.COLS + '\n')
        return board

if __name__ == "__main__":
    print('\n'+'TIC-TAC-TOE GAME'.center(40, '='))
    p1 = input('Player 1 Name: ')
    p2 = input('Player 2 Name: ')
    print()
    GAME = TicTacToe(p1, p2)
    GAME.start_session()
