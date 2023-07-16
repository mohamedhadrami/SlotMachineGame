
import os, time, cache_mgm, random
from Board import Board

MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3
NUM_OF_SYMBOLS = 3

game_start_time = time.strftime("%m%d%Y-%H%M%S", time.localtime())
CACHE_PATH = f"./cache/{game_start_time}.pickle"

user_board = Board(NUM_OF_SYMBOLS)


# GAME FUNCTIONS

def get_deposit() -> int:
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a number.")
    return amount

def display_previous_games(data: dict) -> None:
    saved_games = list(data.keys())
    i = 1
    for game in saved_games:
        print(f"{i}. {game}")
        print(f"\tWinnings: {data[game]['gain']}")
        print(f"\tRounds: {len(data[game]['rounds'])}")

def spin(balance: float, bet: int) -> int:
    board = user_board.get_board()
    data, wins = user_board()
    winnings = -bet
    #if wins[0][1] > 0 or wins[1][1] > 0:
    #    winnings += (wins[0][1] + wins[1][1]) * 0.25 * bet
    if wins[0][0] > 0 or wins[1][0] > 0:
        winnings += (wins[0][0] + wins[1][0]) * 0.5 * bet
    if wins[2][0] > 0:
        winnings += wins[2][0] * 1.5 * bet
    
    balance = balance + winnings
    return data, balance, winnings

def main(balance: int) -> None:
    bet_data = {}
    counter = 1
    deposit = balance
    while True:
        try:
            print(f"Current balance: ${balance}")
            bet = input("How much do you want to bet? (Press q to exit)\t")
            if bet == 'q':
                raise KeyboardInterrupt
            elif not bet.isdigit():
                print(f"Your bet must be an integer.")
            elif int(bet) > balance:
                print("You don't have enough to bet that much.")
            else:
                data, balance, winnings = spin(balance, int(bet))
                round_name = "round_" + str(counter)
                bet_data[round_name] = {"data": data, "bet": int(bet), "winnings": winnings}
                counter += 1
        except KeyboardInterrupt:
            print(f"\nYou came in with {deposit} and you walked out with {balance}. \
                  \nYour total gains are {balance - deposit}")
            cache_mgm.save_game_data(CACHE_PATH, user_board, deposit, balance, bet_data)
            break



if __name__=="__main__":
    data = cache_mgm.check_cache()
    display_previous_games(data)
    '''
    new_game_bool = input("Do you want to load a game? \
                          \nIf so, input the number of the file. \
                          \nOtherwise press ENTER.")
    if new_game_bool:
        main(balance)
    else:
        balance = get_deposit()
        main(balance)
    '''
    balance = get_deposit()
    main(balance)

