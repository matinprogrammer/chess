from enum import Enum
from .abstract import Piece


__all__ = ["PieceName", "Pawn", "Rook", "Knight", "Bishop", "Queen", "King"]


class PieceName(Enum):
    PAWN = "pawn"
    ROOK = "rook"
    KNIGHT = "knight"
    BISHOP = "bishop"
    QUEEN = "queen"
    KING = "king"


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
