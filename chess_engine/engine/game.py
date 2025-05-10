"""
This module is responsible for managing the Chess class,
which handles the turn order and game history rules for chess.
"""

from board import Board
from piece.color import ColorName
from piece.abstract import MoveInfo

TURN_START_INDEX = 1


class GameError(Exception):
    """
    Exception raised for errors in the game state, such as invalid moves or game logic errors.
    """


class Game:
    """
    This class is responsible for managing the turn order and the game history.
    """

    def __init__(self):
        self.board = Board()
        self.turn = ColorName.WHITE
        self.turn_index = TURN_START_INDEX
        self.move_history: list[MoveInfo] = []

    def switch_turn(self) -> None:
        """
        Switches the current player's turn.

        If the turn is White, it changes to Black, and vice versa. It also updates
        the turn index, incrementing it by 1 to track the number of turns.
        """
        self.turn = ColorName.BLACK if self.turn == ColorName.WHITE else ColorName.WHITE
        self.turn_index += 1

    def __str__(self) -> str:
        return f"Turn: {self.turn.value} in_move: {(self.turn_index + 1) // 2}\n" + str(self.board)
