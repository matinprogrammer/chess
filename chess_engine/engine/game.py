from board import Board
from piece.color import ColorName
from piece.abstract import MoveInfo


class GameError(Exception):
    pass


class Game:
    def __init__(self):
        self.board = Board()
        self.turn = ColorName.WHITE
        self.turn_index = 1
        self.move_history: list[MoveInfo] = []

    def switch_turn(self) -> None:
        self.turn = ColorName.BLACK if self.turn == ColorName.WHITE else ColorName.WHITE
        self.turn_index += 1

    def __str__(self) -> str:
        return f"Turn: {self.turn.value} in_move: {(self.turn_index + 1) // 2}\n" + str(self.board)


game = Game()
print(game)
