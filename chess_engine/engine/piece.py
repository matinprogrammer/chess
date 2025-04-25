from abc import ABC, abstractmethod
from typing import List, Tuple, Union

PAWN = "pawn"
ROOK = "rook"
KNIGHT = "knight"
BISHOP = "bishop"
QUEEN = "queen"
KING = "king"


class PieceCreatorError(Exception):
    pass


class Piece(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_moves(self):
        pass

    @abstractmethod
    def get_attacks(self):
        pass


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
    def create_piece(self) -> Piece:
        pass


class PawnCreator(PieceCreator):
    def create_piece(self) -> Piece:
        return Pawn()


class RookCreator(PieceCreator):
    def create_piece(self) -> Piece:
        return Rook()


class KnightCreator(PieceCreator):
    def create_piece(self) -> Piece:
        return Knight()


class BishopCreator(PieceCreator):
    def create_piece(self) -> Piece:
        return Bishop()


class QueenCreator(PieceCreator):
    def create_piece(self) -> Piece:
        return Queen()


class KingCreator(PieceCreator):
    def create_piece(self) -> Piece:
        return King()


def piece_creator(piece: str) -> Piece:
    pieces = {
        PAWN: PawnCreator,
        ROOK: RookCreator,
        KNIGHT: KnightCreator,
        BISHOP: BishopCreator,
        QUEEN: QueenCreator,
        KING: KingCreator,
    }
    result = pieces.get(piece, None)
    if result is None:
        raise PieceCreatorError(f"Unknown piece: {piece}")
    return result().create_piece()
