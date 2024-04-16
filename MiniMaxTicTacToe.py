#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""My implementation of Minimax AI Algorithm in Tic Tac Toe. """

import random
import sys
import time





# Constants
board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_'],
]
playerConstant = ''
computerConstant = ''
startFirst = ''


# In[2]:


def ClearBoard(board):
    '''This function clear the board and make it ready to play again!!'''
    for row in range(3):
        for col in range(3):
            board[row][col] = '_'


# In[3]:


def DisplayBoard(board):
    '''This function print the board to the console'''
    print(board)
    print('----' * 12 + '-')
    print('/', '/', '/', '/', sep='\t\t')
    print('/', board[0][0], '/', board[0][1], '/', board[0][2], '/', sep="\t")
    print('/', '/', '/', '/', sep='\t\t')
    print('----' * 12 + '-')
    print('/', '/', '/', '/', sep='\t\t')
    print('/', board[1][0], '/', board[1][1], '/', board[1][2], '/', sep="\t")
    print('/', '/', '/', '/', sep='\t\t')
    print('----' * 12 + '-')
    print('/', '/', '/', '/', sep='\t\t')
    print('/', board[2][0], '/', board[2][1], '/', board[2][2], '/', sep="\t")
    print('/', '/', '/', '/', sep='\t\t')
    print('----' * 12 + '-')
    print('_' * 70)
    pass


# In[4]:


def isTherePosistionsLeft(board):
    '''The function browses the board and return if there is a free squares'''
    for row in board:
        for col in row:
            if col == '_':
                return True
    return False


# In[5]:


def MakeListOfFreeFields(board):
    '''This function return a list with free fields in the board'''
    free = []
    count = 1
    for row in range(3):
        for col in range(3):
            if board[row][col] == '_':
                free.append(count)
            count += 1
    return free


# In[6]:


def ThereIsWinner(board):
    '''the function analyzes the board status in order to check if the player using 'O's or 'X's has won the game'''
    # Checking Rows for X or O victory.
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == playerConstant:
                return +10
            elif board[row][0] == computerConstant:
                return -10

    # Checking Columns for X or O victory.
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == playerConstant:
                return +10
            elif board[0][col] == computerConstant:
                return -10

    # Checking Diagonals for X or O victory.
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == playerConstant:
            return +10
        elif board[0][0] == computerConstant:
            return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == playerConstant:
            return +10
        elif board[0][2] == computerConstant:
            return -10

    # if non has win return 0
    return 0


# In[7]:


def ConvertToBoardPosition(pos):
    '''This function convert the user move for range (1 - 9) to positions row(0-2) and col(0-2)'''
    row = pos // 3
    col = pos % 3
    if not col:
        row -= 1
        col = 2
    else:
        col -= 1
    return [row, col]


# In[8]:


def EnterUserMove(board):
    '''Asks the user about their move, checks the input, and updates the board according to the user's decision'''

    free = MakeListOfFreeFields(board)
    if not free or ThereIsWinner(board):
        return

    while True:
        try:
            pos = int(input('Enter the position you want in between (1 - 9): '))
            if pos < 1 or pos > 9:
                print('Invalid position. Try Again!!')
            elif pos in free:
                row, col = ConvertToBoardPosition(pos)
                board[row][col] = playerConstant
                print('Computer Turn ... ')
                break
            else:
                print('This position already taken. Try Again!!')
        except KeyboardInterrupt:
            sys.exit()
        except:
            print('Only a "Number" Can Be Entered without spaces.')


# In[9]:


def bestComputerMove(board):
    '''This function will return tuple with the best possible move for the computer'''
    time.sleep(1)
    free = MakeListOfFreeFields(board)
    if len(free) == 0 or ThereIsWinner(board):
        return
    if len(free) == 9:
        row, col = ConvertToBoardPosition(random.randint(1, 9))
    else:
        move = minimax(board, len(free), startFirst)
        row, col = move[0], move[1]
    board[row][col] = computerConstant
    print('Your Turn ... ')


# In[10]:


def minimax(board, depth, isPlayer):
    '''This function applyes the AI minimax algorithem to find the best move for the computer'''

    if isPlayer:
        best = [-1, -1, float('inf')]
    else:
        best = [-1, -1, float('-inf')]

    bestVal = ThereIsWinner(board)
    if depth == 0 or bestVal > 0 or bestVal < 0:
        return [-1, -1, bestVal]

    for pos in MakeListOfFreeFields(board):
        row, col = ConvertToBoardPosition(pos)
        board[row][col] = computerConstant if isPlayer else playerConstant
        score = minimax(board, depth - 1, not isPlayer)
        board[row][col] = '_'
        if isPlayer:
            if score[2] < best[2]:
                best = score  # max value
                score[0], score[1] = row, col
        else:
            if score[2] > best[2]:
                best = score  # min value
                score[0], score[1] = row, col
    return best


# In[11]:


if __name__ == '__main__':

    while True:
        try:
            playerConstant = input('X or O:\nYou Choosed:').upper()
            if playerConstant == 'O' or playerConstant == 'X':
                break;
        except KeyboardInterrupt:
            sys.exit()

    computerConstant = 'O' if playerConstant == 'X' else 'X'

    while True:
        try:
            startFirst = input('Start First (Y,N):\nYou Choosed:').upper()
            if startFirst == 'Y' or startFirst == 'N':
                startFirst = True if startFirst == 'Y' else False
                break;
        except KeyboardInterrupt:
            sys.exit()

    while not ThereIsWinner(board) and len(MakeListOfFreeFields(board)):
        if not startFirst:
            startFirst = not startFirst
            bestComputerMove(board)
            DisplayBoard(board)
        EnterUserMove(board)
        DisplayBoard(board)
        bestComputerMove(board)
        DisplayBoard(board)
    if ThereIsWinner(board) > 0:
        print('YOU WIN !!!')
    elif ThereIsWinner(board) < 0:
        print('YOU LOSE !!!')
    else:
        print('!! DRAW !!')