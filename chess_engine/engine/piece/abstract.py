from abc import ABC, abstractmethod
from .color import PieceColor
from .position import PiecePosition
from typing import Callable, Generator, TypeAlias, List, Tuple, Type
from pydantic import BaseModel, ConfigDict

MoveGenerator: TypeAlias = Callable[[PiecePosition], Generator[PiecePosition, None, None]]


class PieceError(Exception):
    pass


class MoveInfo(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    from_pos: PiecePosition
    to_pos: List[List[PiecePosition]]
    is_attack: bool = False

    def __str__(self):
        positions = []
        for group_pos in self.to_pos:
            for pos in group_pos:
                positions.append(str(pos))

        return f"from position: {self.from_pos}, to position: {', '.join(positions)}, is attack: {self.is_attack}"


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
    def get_moves(self) -> MoveInfo:
        pass

    @abstractmethod
    def get_attacks(self) ->MoveInfo:
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

    def _get_moves_by_directions(self, directions: List[MoveGenerator]) -> MoveInfo:
        result = {"from_pos": self.position, "to_pos": []}

        for direction in directions:
            path = []
            gen = direction(self.position)
            for pos in gen:
                path.append(pos)
            result["to_pos"].append(path)

        return MoveInfo(**result)

    def _get_moves_by_offset(self, offset: List[Tuple[int, int]]) -> MoveInfo:
        result = {"from_pos": self.position, "to_pos": []}

        for dr, dc in offset:
            pos = self.position.offset(self.position, (dr, dc))
            if pos is not None:
                result["to_pos"].append([pos])
        return MoveInfo(**result)