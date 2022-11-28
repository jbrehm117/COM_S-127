# Joseph Brehm             11-21-2022
# Assignment #6 Naval Battle


import gameBoard
import gamePlay


def main():
    """This is the main function of the game. It controls the flow/ execution of the entire script.
    """
    gameOver = False

    gameboardChoice = 0
    humanGameBoard = None
    targetBoard = None
    computerGameBoard = None

    numHumanTargets = 0
    numComputerTargets = 0

    print("Welcome to Naval Battle!")
    print()

    print("By: Joseph Brehm")
    print("[COM S 127 D]")
    print()

    while gameOver == False:
        choice = input("[p]lay, [i]nstructions, or [q]uit?: ")
        print()
        if choice == "p":
            gameboardChoice = gameBoard.chooseHumanGameBoard()
            humanGameBoard, numHumanTargets = gameBoard.loadGameBoard(
                gameboardChoice)
            computerGameBoard = gameBoard.chooseComputerGameBoard()
            computerGameBoard, numComputerTargets = gameBoard.loadGameBoard(
                computerGameBoard)
            targetBoard = gameBoard.loadTargetBoard()
            gamePlay.runGame(humanGameBoard, targetBoard,
                             computerGameBoard, numHumanTargets, numComputerTargets)
        elif choice == "i":
            print("BattleShip Rules:")
            print("Battleship is played with two boards, one for the player and one for the computer. When it is your turn, choose a coordinate point (row, col) \nwhere you think that yout opponent might have a battleship. if the computer's ship is in that location, a hit will be called.\nYour main objective is to sink all the computers ships before it does.")
            pass
        elif choice == "q":
            gameOver = True
            print("Goodbye and see you next time!")
            pass
        else:
            print()
            print("Please enter [p], [i], or [q]...")
            print()


if __name__ == "__main__":
    main()
