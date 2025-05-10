"""
This module implements the Factory Method pattern to create chess piece instances.
Each type of piece has its own dedicated creator class that handles instantiation.
A generic function `piece_creator` is provided to simplify the creation of any piece
based on its name, color, and position.
"""

from abc import ABC, abstractmethod
from typing import Dict, Type

from .pieces import Pawn, Rook, Knight, Bishop, Queen, King, PieceName
from .color import ColorName, PieceColor
from .abstract import Piece
from .position import PiecePosition


class PieceCreatorError(Exception):
    """
    Custom exception raised when piece creation fails due to invalid input or unknown piece type.
    """


class PieceCreator(ABC): # pylint: disable=too-few-public-methods
    """
    Abstract base class for chess piece creators. Requires implementation of create_piece().
    """
    @abstractmethod
    def create_piece(self, color: PieceColor, position: PiecePosition) -> Piece:
        """
        Creates and returns a chess piece instance with the given color and position.
        """

    @staticmethod
    def _validate_data(color: PieceColor, position: PiecePosition) -> None:
        """
        Validates that the provided color and position are of correct types.
        """
        if not isinstance(color, PieceColor):
            raise PieceCreatorError(f"color must be instance of {PieceColor.__name__}")
        if not isinstance(position, PiecePosition):
            raise PieceCreatorError(f"position must be instance of {PiecePosition.__name__}")


class PawnCreator(PieceCreator): # pylint: disable=too-few-public-methods
    """
    Concrete creator for Pawn pieces.
    """
    def create_piece(self, color: PieceColor, position: PiecePosition) -> Piece:
        PieceCreator._validate_data(color, position)
        return Pawn(color, position)


class RookCreator(PieceCreator): # pylint: disable=too-few-public-methods
    """
    Concrete creator for Rook pieces.
    """
    def create_piece(self, color: PieceColor, position: PiecePosition) -> Piece:
        PieceCreator._validate_data(color, position)
        return Rook(color, position)


class KnightCreator(PieceCreator): # pylint: disable=too-few-public-methods
    """
    Concrete creator for Knight pieces.
    """
    def create_piece(self, color: PieceColor, position: PiecePosition) -> Piece:
        PieceCreator._validate_data(color, position)
        return Knight(color, position)


class BishopCreator(PieceCreator): # pylint: disable=too-few-public-methods
    """
    Concrete creator for Bishop pieces.
    """
    def create_piece(self, color: PieceColor, position: PiecePosition) -> Piece:
        PieceCreator._validate_data(color, position)
        return Bishop(color, position)


class QueenCreator(PieceCreator): # pylint: disable=too-few-public-methods
    """
    Concrete creator for Queen pieces.
    """
    def create_piece(self, color: PieceColor, position: PiecePosition) -> Piece:
        PieceCreator._validate_data(color, position)
        return Queen(color, position)


class KingCreator(PieceCreator): # pylint: disable=too-few-public-methods
    """
    Concrete creator for King pieces.
    """
    def create_piece(self, color: PieceColor, position: PiecePosition) -> Piece:
        PieceCreator._validate_data(color, position)
        return King(color, position)


def piece_creator(piece: PieceName, color: ColorName, row: int, column: int) -> Piece:
    """
    Factory function that creates a chess piece based on its type, color, and position.

    Args:
        piece (PieceName): The name/type of the piece (e.g., KING, QUEEN).
        color (ColorName): The color of the piece (e.g., WHITE, BLACK).
        row (int): The row coordinate of the piece.
        column (int): The column coordinate of the piece.

    Returns:
        Piece: An instance of the specified chess piece.

    Raises:
        PieceCreatorError: If the piece type is unknown or input data is invalid.
    """
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
