from abc import ABC, abstractmethod
from typing import Dict, Type
from .pieces import *
from .color import *
from .abstract import Piece


class PieceCreatorError(Exception):
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
