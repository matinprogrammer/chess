from abc import ABC, abstractmethod
from typing import Dict, Type
from .pieces import *
from .color import *
from .abstract import Piece
from .position import *


class PieceCreatorError(Exception):
    pass


class PieceCreator(ABC):
    @abstractmethod
    def create_piece(self, color: PieceColor, position: PiecePosition) -> Piece:
        pass

    @staticmethod
    def _validate_data(color: PieceColor, position: PiecePosition) -> None:
        if not isinstance(color, PieceColor):
            raise PieceCreatorError(f"color must be instance of {PieceColor.__name__}")
        if not isinstance(position, PiecePosition):
            raise PieceCreatorError(f"position must be instance of {PiecePosition.__name__}")


class PawnCreator(PieceCreator):
    def create_piece(self, color: PieceColor, position: PiecePosition) -> Piece:
        PieceCreator._validate_data(color, position)
        return Pawn(color, position)


class RookCreator(PieceCreator):
    def create_piece(self, color: PieceColor, position: PiecePosition) -> Piece:
        PieceCreator._validate_data(color, position)
        return Rook(color, position)


class KnightCreator(PieceCreator):
    def create_piece(self, color: PieceColor, position: PiecePosition) -> Piece:
        PieceCreator._validate_data(color, position)
        return Knight(color, position)


class BishopCreator(PieceCreator):
    def create_piece(self, color: PieceColor, position: PiecePosition) -> Piece:
        PieceCreator._validate_data(color, position)
        return Bishop(color, position)


class QueenCreator(PieceCreator):
    def create_piece(self, color: PieceColor, position: PiecePosition) -> Piece:
        PieceCreator._validate_data(color, position)
        return Queen(color, position)


class KingCreator(PieceCreator):
    def create_piece(self, color: PieceColor, position: PiecePosition) -> Piece:
        PieceCreator._validate_data(color, position)
        return King(color, position)


def piece_creator(piece: PieceName, color: ColorName, row: int, column: int) -> Piece:
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
    piece_position = PiecePosition(row, column)
    return piece_creator_class().create_piece(piece_color, piece_position)
