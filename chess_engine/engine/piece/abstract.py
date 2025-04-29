from abc import ABC, abstractmethod
from .color import PieceColor
from .position import PiecePosition


class PieceError(Exception):
    pass


class Piece(ABC):
    def __init__(self, color: PieceColor, position: PiecePosition) -> None:
        self.color = color
        self.position = position
        self._is_die = False
        self._has_moved = False
        self.name = color.color.value + self.__class__.__name__.lower()

    @property
    def is_die(self) -> bool:
        return self._is_die

    @is_die.setter
    def is_die(self, value: bool) -> None:
        raise PieceError("is_die cannot be set directly; use .kill() method instead.")

    @is_die.deleter
    def is_die(self):
        raise PieceError("is_die cannot be deleted")

    def kill(self) -> None:
        self._is_die = True

    @property
    def has_moved(self) -> bool:
        return self._has_moved

    @has_moved.setter
    def has_moved(self, value: bool) -> None:
        raise PieceError("has_moved cannot be set directly; use .move() method instead.")

    @has_moved.deleter
    def has_moved(self):
        raise PieceError("has_moved cannot be deleted")

    def move(self) -> None:
        self._has_moved = True

    @abstractmethod
    def get_moves(self):
        pass

    @abstractmethod
    def get_attacks(self):
        pass

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}"
            f"-{self.color}"
            f"-{self.position}"
            f"-{'die' if self.is_die else 'alive'}"
            f"-{'moved' if self.is_die else 'unmoved'}"
        )

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.color=}, {self.position=}, {self.is_die=}, {self.has_moved=})"
