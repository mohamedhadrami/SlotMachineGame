
import os, time, cache_mgm
from Board import Board

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3
NUM_OF_SYMBOLS = 3

game_start_time = time.strftime("%m%d%Y-%H%M%S", time.localtime())
os.mkdir('./cache/' + game_start_time)
CACHE_PATH = os.path.dirname(f"./cache/{game_start_time}")

balance = 500
initial_balance = balance
user_board = Board(NUM_OF_SYMBOLS)


# GAME FUNCTIONS

def deposit() -> int:
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

def spin(balance: float, bet: int) -> int:
    board = user_board.get_board()
    data, wins = board()
    winnings = -bet
    #if wins[0][1] > 0 or wins[1][1] > 0:
    #    winnings += (wins[0][1] + wins[1][1]) * 0.25 * bet
    if wins[0][0] > 0 or wins[1][0] > 0:
        winnings += (wins[0][0] + wins[1][0]) * 0.5 * bet
    if wins[2][0] > 0:
        winnings += wins[2][0] * 1.5 * bet
    
    balance = balance + winnings
    return data, balance

def main() -> None:
    global balance
    deposit()
    while True:
        try:
            print(f"Current balance: ${balance}")
            bet = input("How much do you want to bet? (Press q to exit)\t")
            if bet == 'q':
                break
            elif not bet.isdigit():
                print(f"Your bet must be an integer.")
            elif int(bet) > balance:
                print("You don't have enough to bet that much.")
            else:
                data, balance = spin(balance, int(bet))

        except KeyboardInterrupt:
            print(f"\nYou came in with {initial_balance} and you walked out with {balance}. \
                  \nYour total gains are {balance - initial_balance}")
            break



if __name__=="__main__":
    cache_mgm.check_cache()
    #main()


