from abc import ABC, abstractmethod
from .color import PieceColor
from .position import PiecePosition


class Piece(ABC):
    def __init__(self, color: PieceColor, position: PiecePosition) -> None:
        self.color = color
        self.position = position

    @abstractmethod
    def get_moves(self):
        pass

    @abstractmethod
    def get_attacks(self):
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}-{self.color}-{self.position}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.color=}, {self.position=})"
