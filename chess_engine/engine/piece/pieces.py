"""
This module defines all chess pieces and their movement rules.

Includes:
- Enum `PieceName` for identifying piece types.
- Constants for unicode piece icons.
- Piece classes (`Pawn`, `Rook`, `Knight`, `Bishop`, `Queen`, `King`) inheriting from `Piece` base class.
Each piece class implements its own movement and attack logic.
"""

from enum import Enum
from typing import List

from .abstract import Piece, MoveInfo, MoveGenerator
from .color import ColorName
from .position import PiecePosition

__all__ = ["PieceName", "Pawn", "Rook", "Knight", "Bishop", "Queen", "King"]


class PieceName(Enum):
    """
    Enum representing the name of a chess piece.
    """
    PAWN = "pawn"
    ROOK = "rook"
    KNIGHT = "knight"
    BISHOP = "bishop"
    QUEEN = "queen"
    KING = "king"


PAWN_WHITE_ICON = '♟'
PAWN_BLACK_ICON = '♙'

ROOK_WHITE_ICON = '♜'
ROOK_BLACK_ICON = '♖'

KNIGHT_WHITE_ICON = '♞'
KNIGHT_BLACK_ICON = '♘'

BISHOP_WHITE_ICON = '♝'
BISHOP_BLACK_ICON = '♗'

QUEEN_WHITE_ICON = '♛'
QUEEN_BLACK_ICON = '♕'

KING_WHITE_ICON = '♚'
KING_BLACK_ICON = '♔'

FROM_POS_KEY = 'from_pos'
TO_POS_KEY = 'to_pos'
IS_ATTACK_KEY = 'is_attack'


class Pawn(Piece):
    """
    Represents a Pawn piece in a chess game.

    The Pawn piece can move forward one square or two squares (if it hasn't moved before),
    and it attacks diagonally. The movement and attack logic depend on the color of the Pawn
    (White or Black).
    """

    @property
    def icon(self):
        return PAWN_WHITE_ICON if self.color.color == ColorName.WHITE else PAWN_BLACK_ICON

    def get_moves(self):
        result = {FROM_POS_KEY: self.position, TO_POS_KEY: [[]]}

        if self.color.color == ColorName.WHITE:
            pos_gen = PiecePosition.move_up(self.position)
        else:
            pos_gen = PiecePosition.move_down(self.position)

        pos1 = next(pos_gen, None)
        if pos1:
            result[TO_POS_KEY][0].append(pos1)

        if not self.has_moved:
            pos2 = next(pos_gen, None)
            if pos2:
                result[TO_POS_KEY][0].append(pos2)
        return MoveInfo(**result)

    def get_attacks(self):
        result = {FROM_POS_KEY: self.position, TO_POS_KEY: [], IS_ATTACK_KEY: True}

        if self.color.color == ColorName.WHITE:
            directions: List[MoveGenerator] = [PiecePosition.move_up_right, PiecePosition.move_up_left]
        else:
            directions: List[MoveGenerator] = [PiecePosition.move_down_right, PiecePosition.move_down_left]

        for direction in directions:
            pos = next(direction(self.position), None)
            if pos:
                result[TO_POS_KEY].append([pos])

        return MoveInfo(**result)


class Rook(Piece):
    """
    Represents a Rook piece in a chess game.

    The Rook can move horizontally or vertically across the board. Its movement and attack
    are defined by these directions.
    """

    @property
    def icon(self):
        return ROOK_WHITE_ICON if self.color.color == ColorName.WHITE else ROOK_BLACK_ICON

    def get_moves(self):
        directions = [
            PiecePosition.move_up,
            PiecePosition.move_right,
            PiecePosition.move_down,
            PiecePosition.move_left
        ]
        return self._get_moves_by_directions(directions)

    def get_attacks(self):
        return self.get_moves()


class Knight(Piece):
    """
    Represents a Knight piece in a chess game.

    The Knight moves in an "L" shape: two squares in one direction and one square perpendicular.
    Its movement is unique compared to other pieces.
    """

    @property
    def icon(self):
        return KNIGHT_WHITE_ICON if self.color.color == ColorName.WHITE else KNIGHT_BLACK_ICON

    def get_moves(self):
        offset = [
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1)
        ]
        return self._get_moves_by_offset(offset)

    def get_attacks(self):
        return self.get_moves()


class Bishop(Piece):
    """
    Represents a Bishop piece in a chess game.

    The Bishop moves diagonally across the board in all four diagonal directions.
    """

    @property
    def icon(self):
        return BISHOP_WHITE_ICON if self.color.color == ColorName.WHITE else BISHOP_BLACK_ICON

    def get_moves(self):
        directions = [
            PiecePosition.move_up_right,
            PiecePosition.move_down_right,
            PiecePosition.move_down_left,
            PiecePosition.move_up_left
        ]
        return self._get_moves_by_directions(directions)

    def get_attacks(self):
        return self.get_moves()


class Queen(Piece):
    """
    Represents a Queen piece in a chess game.

    The Queen combines the movement of both the Rook and the Bishop, moving horizontally,
    vertically, and diagonally in all directions.
    """

    @property
    def icon(self):
        return QUEEN_WHITE_ICON if self.color.color == ColorName.WHITE else QUEEN_BLACK_ICON

    def get_moves(self):
        directions = [
            PiecePosition.move_up,
            PiecePosition.move_up_right,
            PiecePosition.move_right,
            PiecePosition.move_down_right,
            PiecePosition.move_down,
            PiecePosition.move_down_left,
            PiecePosition.move_left,
            PiecePosition.move_up_left
        ]
        return self._get_moves_by_directions(directions)

    def get_attacks(self):
        return self.get_moves()


class King(Piece):
    """
    Represents a King piece in a chess game.

    The King can move one square in any direction. Its movement is limited to adjacent squares.
    """

    @property
    def icon(self):
        return KING_WHITE_ICON if self.color.color == ColorName.WHITE else KING_BLACK_ICON

    def get_moves(self):
        offset = [
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1)
        ]
        return self._get_moves_by_offset(offset)

    def get_attacks(self):
        return self.get_moves()
