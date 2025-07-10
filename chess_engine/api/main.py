from fastapi import FastAPI
from chess_engine.engine.game import Game

app = FastAPI()
game_instance = Game()

@app.get("/")
def get_game_status():
    return {
        "chess": str(game_instance.board.serialize()),
    }
