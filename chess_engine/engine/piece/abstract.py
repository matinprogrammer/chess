from abc import ABC, abstractmethod
from .color import PieceColor


class Piece(ABC):
    def __init__(self, color: PieceColor) -> None:
        self.color = color

    @abstractmethod
    def get_moves(self):
        pass

    @abstractmethod
    def get_attacks(self):
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}-{self.color}"

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} {self.color=}>"
