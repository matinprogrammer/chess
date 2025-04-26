from abc import ABC, abstractmethod
from typing import Dict, Type
from enum import Enum

class PieceName(Enum):
    PAWN = "pawn"
    ROOK = "rook"
    KNIGHT = "knight"
    BISHOP = "bishop"
    QUEEN = "queen"
    KING = "king"


class ColorName(Enum):
    WHITE = "white"
    BLACK = "black"


class PieceColorError(Exception):
    pass


class PieceColor:
    def __init__(self, color: ColorName) -> None:
        self.color = color

    @property
    def color(self) -> ColorName:
        return self._color

    @color.setter
    def color(self, value: ColorName) -> None:
        if not isinstance(value, ColorName):
            raise PieceColorError(f"Color must be a string or Color enum, got {type(value)}")
        self._color = value

    @color.deleter
    def color(self) -> None:
        raise PieceColorError("Color cannot be deleted")

    def __str__(self) -> str:
        return self._color.value

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} color={self._color}>"


class PieceCreatorError(Exception):
    pass


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


class Pawn(Piece):
    def get_moves(self):
        pass

    def get_attacks(self):
        pass


class Rook(Piece):
    def get_moves(self):
        pass

    def get_attacks(self):
        pass


class Knight(Piece):
    def get_moves(self):
        pass

    def get_attacks(self):
        pass


class Bishop(Piece):
    def get_moves(self):
        pass

    def get_attacks(self):
        pass


class Queen(Piece):
    def get_moves(self):
        pass

    def get_attacks(self):
        pass


class King(Piece):
    def get_moves(self):
        pass

    def get_attacks(self):
        pass


class PieceCreator(ABC):
    @abstractmethod
    def create_piece(self, color: PieceColor) -> Piece:
        pass

    @staticmethod
    def _validate_data(color: PieceColor) -> None:
        if not isinstance(color, PieceColor):
            raise PieceCreatorError(f"color must be instance of {PieceColor.__name__}")


class PawnCreator(PieceCreator):
    def create_piece(self, color: PieceColor) -> Piece:
        PieceCreator._validate_data(color)
        return Pawn(color)


class RookCreator(PieceCreator):
    def create_piece(self, color: PieceColor) -> Piece:
        PieceCreator._validate_data(color)
        return Rook(color)


class KnightCreator(PieceCreator):
    def create_piece(self, color: PieceColor) -> Piece:
        PieceCreator._validate_data(color)
        return Knight(color)


class BishopCreator(PieceCreator):
    def create_piece(self, color: PieceColor) -> Piece:
        PieceCreator._validate_data(color)
        return Bishop(color)


class QueenCreator(PieceCreator):
    def create_piece(self, color: PieceColor) -> Piece:
        PieceCreator._validate_data(color)
        return Queen(color)


class KingCreator(PieceCreator):
    def create_piece(self, color: PieceColor) -> Piece:
        PieceCreator._validate_data(color)
        return King(color)


def piece_creator(piece: PieceName, color: ColorName) -> Piece:
    pieces: Dict[PieceName, Type[PieceCreator]] = {
        PieceName.PAWN: PawnCreator,
        PieceName.ROOK: RookCreator,
        PieceName.KNIGHT: KnightCreator,
        PieceName.BISHOP: BishopCreator,
        PieceName.QUEEN: QueenCreator,
        PieceName.KING: KingCreator,
    }
    piece_creator_class = pieces.get(piece)

    if piece_creator_class is None:
        raise PieceCreatorError(f"Unknown piece: {piece}")

    piece_color = PieceColor(color)
    return piece_creator_class().create_piece(piece_color)
