
import os, pickle
from Board import Board

CACHE_PATH = "./cache/"

def save_game_data(path: os.path, 
                   board: Board, 
                   deposit: float,
                   balance: float,
                   bets: list) -> None:
    game_data = {"board": board, 
                 "deposit": deposit,
                 "balance": balance,
                 "gain": balance - deposit,
                 "rounds": bets}
    with open(path, "wb") as file:
        pickle.dump(game_data, file)

def load_game_data(game_path: os.path) -> dict:
    if os.path.exists(CACHE_PATH + game_path):
        path = CACHE_PATH + game_path
        with open(path, "rb") as f:
            game_data = pickle.load(f)
            return game_data
    else:
        return 0.0

def check_cache() -> list:
    saved_game = os.listdir(CACHE_PATH)
    saved_game.sort()
    if len(saved_game) > 5:
        os.remove(CACHE_PATH + saved_game[0])
        saved_game = os.listdir(CACHE_PATH)
    saved_game_data = {}
    for file in saved_game:
        data = load_game_data(file)
        saved_game_data[file] = data
    return saved_game_data