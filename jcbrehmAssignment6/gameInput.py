# Joseph Brehm             11-21-2022
# Assignment #6 Naval Battle

import random
import gameBoard


def getHumanInput():
    """This function takes in input from the human for wich row and column they want to attack.

    Returns:
        int, int: row and col are the integer values designating the row and column for the human to attack.
    """
    while True:
        try:
            row = int(input("Row: "))
            while row < 0 or row > gameBoard.GAME_BOARD_HEIGHT - 1:
                print("Invalid input...please input another number")
                row = int(input("Row: "))
            break
        except Exception as e:
            print("ERROR: Please input row as an integer...", e)
            continue
    while True:
        try:
            col = int(input("Col: "))
            while col < 0 or col > gameBoard.GAME_BOARD_WIDTH - 1:
                print("Invalid input...please input another number")
                col = int(input("Column: "))
            break
        except Exception as e:
            print("ERROR: Please input row as an integer...", e)
            continue

    return row, col


def getComputerInput():
    """This function randomly generates input from the computer for which row and column it wants to attack.

    Returns:
        int, int: row and col are the integer values designating the row and column for the computer to attack.
    """
    row = random.randint(0, gameBoard.GAME_BOARD_HEIGHT - 1)
    col = random.randint(0, gameBoard.GAME_BOARD_WIDTH - 1)

    return row, col
