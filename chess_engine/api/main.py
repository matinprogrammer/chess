from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chess_engine.engine.game import Game

app = FastAPI()
game_instance = Game()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_game_status():
    return {
        "chess": str(game_instance.board.serialize()),
    }
