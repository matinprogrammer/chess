"""
This module defines the abstract base class `Piece` for chess pieces, along with helper classes
like `MoveInfo` and related types for managing movement and state.

Includes:
- Piece: Abstract base for all pieces.
- MoveInfo: Structure for move/attack metadata.
- PieceError: Custom exception for piece state errors.
"""

from abc import ABC, abstractmethod
from typing import Callable, Generator, TypeAlias, List, Tuple, Dict

from pydantic import BaseModel, ConfigDict

from .color import PieceColor
from .position import PiecePosition

MoveGenerator: TypeAlias = Callable[[PiecePosition], Generator[PiecePosition, None, None]]


class PieceError(Exception):
    """
    Exception raised for invalid operations on chess pieces.
    """


class MoveInfo(BaseModel):
    """
    Stores movement data of a piece.

    Attributes:
        from_pos: The piece's current position.
        to_pos: A grouped list of possible destination positions.
        is_attack: Whether the move represents an attack.
    """
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
    """
    Abstract base class for all chess pieces.

    Attributes:
        color: The piece's color (black/white).
        position: Current board position.
        is_die: Status if the piece is captured (read-only).
        has_moved: Status if the piece has moved (read-only).
    """
    def __init__(self, color: PieceColor, position: PiecePosition) -> None:
        self.color = color
        self.position = position
        self._is_die = False
        self._has_moved = False
        self.name = color.color.value + self.__class__.__name__.lower()

    @property
    @abstractmethod
    def icon(self):
        """
        Symbolic representation (icon) of the piece.
        """

    @property
    def is_die(self) -> bool:
        """
        property for validate is_die in piece
        """
        return self._is_die

    @is_die.setter
    def is_die(self, value: bool) -> None:
        raise PieceError("is_die cannot be set directly; use .kill() method instead.")

    @is_die.deleter
    def is_die(self):
        raise PieceError("is_die cannot be deleted")

    def kill(self) -> None:
        """
        Marks the piece as captured.
        """
        self._is_die = True

    @property
    def has_moved(self) -> bool:
        """
        property for validate has_moved in piece
        """
        return self._has_moved

    @has_moved.setter
    def has_moved(self, value: bool) -> None:
        raise PieceError("has_moved cannot be set directly; use .move() method instead.")

    @has_moved.deleter
    def has_moved(self):
        raise PieceError("has_moved cannot be deleted")

    def move(self) -> None:
        """
        Marks the piece as having moved.
        """
        self._has_moved = True

    @abstractmethod
    def get_moves(self) -> MoveInfo:
        """
        Returns all possible legal moves.
        """

    @abstractmethod
    def get_attacks(self) ->MoveInfo:
        """
        Returns all possible attack moves.
        """

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
        """
        Helper method to generate moves using directional generators (rook, bishop, queen).
        """
        result = {"from_pos": self.position, "to_pos": []}

        for direction in directions:
            path = []
            gen = direction(self.position)
            for pos in gen:
                path.append(pos)
            result["to_pos"].append(path)

        return MoveInfo(**result)

    def _get_moves_by_offset(self, offset: List[Tuple[int, int]]) -> MoveInfo:
        """
        Helper method to generate moves using coordinate offsets (knight, king).
        """
        result = {"from_pos": self.position, "to_pos": []}

        for dr, dc in offset:
            pos = self.position.offset(self.position, (dr, dc))
            if pos is not None:
                result["to_pos"].append([pos])
        return MoveInfo(**result)

    def serialize(self) -> Dict:
        return {
            "name": self.name,
            "color": self.color.color.value,
            "row": self.position.row,
            "column": self.position.column.number,
            "str_position": str(self.position),
        }