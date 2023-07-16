import cache_mgm, os
from Board import Board

saved_game = os.listdir("./cache")
saved_game.sort()
data = cache_mgm.check_cache()

print(data)
#board = data["board"]
#print(board.symbols)
