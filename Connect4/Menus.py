import GameTypes as gt


def mainMenu():
    end = False
    while not end:
        printMainMenuChoices()
        choice = input("")
        if checkIfChoiceLegal(choice, 3):
            end = linksOfMainMenu(choice)


def singlePlayerMenu():
    end = False
    while not end:
        printSinglePlayerMenuChoices()
        choice = input(" ")
        if checkIfChoiceLegal(choice, 5):
            end = linksOfSinglePlayerMenu(choice)


def linksOfMainMenu(choice):
    choice = int(choice)
    if choice == 1:
        singlePlayerMenu()
    elif choice == 2:
        gt.humanVsHumanGame()
    elif choice == 3:
        return True
    return False


def linksOfSinglePlayerMenu(choice):
    choice = int(choice)
    if choice == 1:
        humanTurn = playFirstOrSecond()
        gt.humanVsRandomGame(humanTurn)
    elif choice == 2:
        humanTurn = playFirstOrSecond()
        gt.humanVsMinMax(humanTurn, 5)
    elif choice == 5:
        return True
    return False


def playFirstOrSecond():
    while True:
        print("press 1 to be first")
        print("press 2 to be second")
        choice = input(" ")
        if checkIfChoiceLegal(choice, 2):
            return int(choice)


def checkIfChoiceLegal(choice, optionNum):
    try:
        choice = int(choice)
        if choice > optionNum or choice <= 0:
            print("Illegal input")
            return False
        return True
    except:
        print("Illegal input")
        return False


def printMainMenuChoices():
    print("Press 1 for singlePlayer")
    print("Press 2 for multiplayer")
    print("Press 3 to quit")


def printSinglePlayerMenuChoices():
    print("Press 1 for random opponent")
    print("Press 2 for minMax opponent")
    print("Press 3 for genetic opponent")
    print("Press 4 for A.I opponent")
    print("Press 5 to quit")
