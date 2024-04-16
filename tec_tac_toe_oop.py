import logging
import random
import sys
import time

from loggings import MultipurposeLogger


class TecTacToe:

    def __init__(self, player: str, computer: str, is_first: bool, logger=None):
        self.__board = [  # authorization - access modifiers
            ['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_'],
        ]
        self.__playerConstant = player
        self.__computerConstant = computer
        self.__startFirst = is_first

        self.logger = logger if logger else logging.getLogger()

    def __get_board(self):  # validation - getter and setter
        return self.__board.copy()

    board = property(  # embedded - property
        fget=__get_board
    )

    def __get_player(self):
        return self.__playerConstant

    player = property(
        fget=__get_player
    )

    def __get_computer(self):
        return self.__computerConstant

    computer = property(
        fget=__get_computer
    )

    def __get_is_first(self):
        return self.__startFirst

    is_first = property(
        fget=__get_is_first
    )

    def clear_board(self, ):
        """This function clear the board and make it ready to play again!!"""
        for row in range(3):
            for col in range(3):
                self.__board[row][col] = '_'

    def display_board(self, ):  # Use this would be a UI
        """This function print the board to the console"""
        # print(self.__board)
        print('----' * 6 + '-')
        print('/', '/', '/', '/', sep='\t\t')
        print('/', self.__board[0][0], '/', self.__board[0][1], '/', self.__board[0][2], '/', sep="\t")
        print('/', '/', '/', '/', sep='\t\t')
        print('----' * 6 + '-')
        print('/', '/', '/', '/', sep='\t\t')
        print('/', self.__board[1][0], '/', self.__board[1][1], '/', self.__board[1][2], '/', sep="\t")
        print('/', '/', '/', '/', sep='\t\t')
        print('----' * 6 + '-')
        print('/', '/', '/', '/', sep='\t\t')
        print('/', self.__board[2][0], '/', self.__board[2][1], '/', self.__board[2][2], '/', sep="\t")
        print('/', '/', '/', '/', sep='\t\t')
        print('----' * 6 + '-')
        print('_' * 32)
        pass

    def is_there_positions_left(self, ):
        """The function browses the board and return if there is a free squares or not."""
        for row in self.__board:
            for col in row:
                if col == '_':
                    return True
        return False

    def list_of_free_fields(self, ):
        """This function return a list with free fields in the board"""
        free = []
        count = 1
        for row in range(3):
            for col in range(3):
                if self.__board[row][col] == '_':
                    free.append(count)
                count += 1
        return free

    def there_is_winner(self, ):
        """the function analyzes the board status in order to check if the player using 'O's or 'X's has won the game"""
        # Checking Rows for X or O victory.
        for row in range(3):
            if self.__board[row][0] == self.__board[row][1] and self.__board[row][1] == self.__board[row][2]:
                if self.__board[row][0] == self.__playerConstant:
                    return +10
                elif self.__board[row][0] == self.__computerConstant:
                    return -10

        # Checking Columns for X or O victory.
        for col in range(3):
            if self.__board[0][col] == self.__board[1][col] and self.__board[1][col] == self.__board[2][col]:
                if self.__board[0][col] == self.__playerConstant:
                    return +10
                elif self.__board[0][col] == self.__computerConstant:
                    return -10

        # Checking Diagonals for X or O victory.
        if self.__board[0][0] == self.__board[1][1] and self.__board[1][1] == self.__board[2][2]:
            if self.__board[0][0] == self.__playerConstant:
                return +10
            elif self.__board[0][0] == self.__computerConstant:
                return -10

        if self.__board[0][2] == self.__board[1][1] and self.__board[1][1] == self.__board[2][0]:
            if self.__board[0][2] == self.__playerConstant:
                return +10
            elif self.__board[0][2] == self.__computerConstant:
                return -10

        # if non has win return 0 # This is a Draw
        return 0

    def convert_to_board_position(self, pos):
        """This function convert the user move for range (1 - 9) to positions row(0-2) and col(0-2)"""
        row = pos // 3
        col = pos % 3
        if not col:
            row -= 1
            col = 2
        else:
            col -= 1
        return [row, col]

    def enter_user_move(self, ):
        """Asks the user about their move, checks the input, and updates the board according to the user's decision"""

        free = self.list_of_free_fields()
        if not free or self.there_is_winner():
            return

        while True:
            try:
                pos = int(input('Enter the position you want in between (1 - 9): '))
                if pos < 1 or pos > 9:
                    self.logger.info('Invalid position. Try Again!!')
                elif pos in free:
                    row, col = self.convert_to_board_position(pos)
                    self.__board[row][col] = self.__playerConstant
                    self.logger.info('Computer Turn ... ')
                    break
                else:
                    self.logger.info('This position already taken. Try Again!!')
            except KeyboardInterrupt:
                sys.exit()  # Directly turn of the program
            except:
                self.logger.error('Only a "Number" Can Be Entered without spaces.')

    def best_computer_move(self, ):
        """This function will return tuple with the best possible move for the computer"""
        time.sleep(1)
        free = self.list_of_free_fields()
        if len(free) == 0 or self.there_is_winner():
            return
        if len(free) == 9:
            row, col = self.convert_to_board_position(random.randint(1, 9))
        else:
            move = self.minimax(len(free), self.__startFirst)
            row, col = move[0], move[1]
        self.__board[row][col] = self.__computerConstant
        self.logger.info('Your Turn ... ')

    def minimax(self, depth, is_player):
        """This function applies the AI minimax algorithm to find the best move for the computer"""

        if is_player:
            best = [-1, -1, float('inf')]
        else:
            best = [-1, -1, float('-inf')]

        best_val = self.there_is_winner()
        if depth == 0 or best_val > 0 or best_val < 0:
            return [-1, -1, best_val]

        for pos in self.list_of_free_fields():
            row, col = self.convert_to_board_position(pos)
            self.__board[row][col] = self.__computerConstant if is_player else self.__playerConstant
            score = self.minimax(depth - 1, not is_player)
            self.__board[row][col] = '_'
            if is_player:
                if score[2] < best[2]:
                    best = score  # max value
                    score[0], score[1] = row, col
            else:
                if score[2] > best[2]:
                    best = score  # min value
                    score[0], score[1] = row, col
        return best

    def play(self):
        while not self.there_is_winner() and len(self.list_of_free_fields()):
            if not self.__startFirst:
                self.__startFirst = not self.__startFirst
                self.best_computer_move()
                self.display_board()
            self.enter_user_move()
            self.display_board()
            self.best_computer_move()
            self.display_board()

        if self.there_is_winner() > 0:
            self.logger.info('YOU WIN !!!')
        elif self.there_is_winner() < 0:
            self.logger.info('YOU LOSE !!!')
        else:
            self.logger.info('!! DRAW !!')


def tec_tac_toe_game_starter():
    logger = MultipurposeLogger(
        name="TecTacToeGameLogger",
        create=True
    )

    logger.info("Selecting the user CHaracter")
    while True:
        try:
            playerConstant = input('X or O:\nYou Choosed:').upper()
            if playerConstant == 'O' or playerConstant == 'X':
                break
        except KeyboardInterrupt:
            logger.error("The program were shut forcefully.")
            sys.exit()
    computerConstant = 'O' if playerConstant == 'X' else 'X'

    logger.info("Selecting whos to start first")
    while True:
        try:
            startFirst = input('Start First (Y,N):\nYou Choosed:').upper()
            if startFirst == 'Y' or startFirst == 'N':
                startFirst = True if startFirst == 'Y' else False
                break
        except KeyboardInterrupt:
            logger.error("The program were shut forcefully.")
            sys.exit()

    game = TecTacToe(
        player=playerConstant,
        computer=computerConstant,
        is_first=startFirst,
        logger=logger
    )
    logger.info("Starting the game")
    game.play()
    logger.info("Done.")


if __name__ == '__main__':

    while True:
        tec_tac_toe_game_starter()
        startFirst = input('Play Again (Y,N):\nYou Chose:').upper()
        if startFirst in ['N', 'NO']:
            break

    # print(game.board)
    # game.clear_board()
    # print(game.board)
    # print(game.there_is_winner())
    # print(game.convert_to_board_position(5))
    # print(game.convert_to_board_position(7))
    # print(game.convert_to_board_position(1))
    # print(game.convert_to_board_position(4))
