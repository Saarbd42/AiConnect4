import game_types as gt


def main_menu():
    end = False
    while not end:
        print_main_menu_choices()
        choice = input("")
        if check_if_choice_legal(choice, 3):
            end = links_of_main_menu(choice)


def single_player_menu():
    end = False
    while not end:
        print_single_player_menu_choices()
        choice = input(" ")
        if check_if_choice_legal(choice, 5):
            end = links_of_single_player_menu(choice)


def links_of_main_menu(choice):
    choice = int(choice)
    if choice == 1:
        single_player_menu()
    elif choice == 2:
        gt.human_vs_human_game()
    elif choice == 3:
        return True
    return False


def links_of_single_player_menu(choice):
    choice = int(choice)
    if choice == 1:
        human_turn = play_first_or_second()
        gt.human_vs_random_game(human_turn)
    elif choice == 2:
        human_turn = play_first_or_second()
        gt.human_vs_min_max(human_turn, 5)
    elif choice == 3:
        human_turn = play_first_or_second()
        gt.human_vs_mtc_game(human_turn, 100)
    elif choice == 5:
        return True
    return False


def play_first_or_second():
    while True:
        print("Press 1 to be first")
        print("Press 2 to be second")
        choice = input(" ")
        if check_if_choice_legal(choice, 2):
            return int(choice)


def check_if_choice_legal(choice, option_num):
    try:
        choice = int(choice)
        if choice > option_num or choice <= 0:
            print("Illegal input")
            return False
        return True
    except:
        print("Illegal input")
        return False


def print_main_menu_choices():
    print("Press 1 for single player")
    print("Press 2 for multiplayer")
    print("Press 3 to quit")


def print_single_player_menu_choices():
    print("Press 1 for random opponent")
    print("Press 2 for minMax opponent")
    print("Press 3 for MTC opponent")
    print("Press 4 for AI opponent")
    print("Press 5 to quit")
