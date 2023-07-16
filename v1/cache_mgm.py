
import os, pickle

CACHE_PATH = "./cache/"

# CACHE MANAGEMENT
def save_game_data(balance: float) -> None:
    game_data = {"balance": balance}
    with open(CACHE_PATH, "wb") as file:
        pickle.dump(game_data, file)

def load_game_data(game_path: os.path) -> any:
    pass

def check_cache() -> list:
    saved_game = os.listdir(CACHE_PATH)
    saved_game.sort()
    if len(saved_game) >= 5:
        os.rmdir(CACHE_PATH + saved_game[0])
    print(saved_game)