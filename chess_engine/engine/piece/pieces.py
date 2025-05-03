from enum import Enum
from .abstract import Piece, MoveInfo, MoveGenerator
from .color import ColorName
from .position import PiecePosition
from typing import List

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
        result = {"from_pos": self.position, "to_pos": [[]]}

        if self.color.color == ColorName.WHITE:
            pos_gen = PiecePosition.move_up(self.position)
        else:
            pos_gen = PiecePosition.move_down(self.position)

        pos1 = next(pos_gen, None)
        if pos1:
            result["to_pos"][0].append(pos1)

        if not self.has_moved:
            pos2 = next(pos_gen, None)
            if pos2:
                result["to_pos"][0].append(pos2)
        return MoveInfo(**result)

    def get_attacks(self):
        result = {"from_pos": self.position, "to_pos": [], 'is_attack': True}

        if self.color.color == ColorName.WHITE:
            directions: List[MoveGenerator] = [PiecePosition.move_up_right, PiecePosition.move_up_left]
        else:
            directions: List[MoveGenerator] = [PiecePosition.move_down_right, PiecePosition.move_down_left]

        for direction in directions:
            pos = next(direction(self.position), None)
            if pos:
                result["to_pos"].append([pos])

        return MoveInfo(**result)


class Rook(Piece):
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
