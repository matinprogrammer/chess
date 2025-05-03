from typing import Dict, Optional, List
from piece.abstract import Piece
from piece.position import PiecePosition
from piece.color import ColorName


class BoardError(Exception):
    pass


class Board:
    def __init__(self):
        self._grid: Dict[int, Piece] = {}
        self.setup_initial_positions()

    def setup_initial_positions(self) -> None:
        self._grid.clear()
        from piece.creators import piece_creator, PieceName

        for col in range(1, 9):
            self._grid[
                PiecePosition.convert_row_column_to_position_number(2, col)
            ] = piece_creator(PieceName.PAWN, ColorName.WHITE, 2, col)

            self._grid[
                PiecePosition.convert_row_column_to_position_number(7, col)
            ] = piece_creator(PieceName.PAWN, ColorName.BLACK, 7, col)

        back_rank = [
            PieceName.ROOK,
            PieceName.KNIGHT,
            PieceName.BISHOP,
            PieceName.QUEEN,
            PieceName.KING,
            PieceName.BISHOP,
            PieceName.KNIGHT,
            PieceName.ROOK
        ]
        for idx, piece_name in enumerate(back_rank, start=1):
            self._grid[
                PiecePosition.convert_row_column_to_position_number(1, idx)
            ] = piece_creator(piece_name, ColorName.WHITE, 1, idx)

            self._grid[
                PiecePosition.convert_row_column_to_position_number(8, idx)
            ] = piece_creator(piece_name, ColorName.BLACK, 8, idx)

    def get_piece_at(self, position: PiecePosition) -> Optional[Piece]:
        return self._grid.get(position.get_position_number())

    def move_piece(self, from_pos: PiecePosition, to_pos: PiecePosition) -> None:
        key_from = from_pos.get_position_number()
        key_to = to_pos.get_position_number()
        piece = self._grid.get(key_from)
        if piece is None:
            raise BoardError(f"No piece at position {from_pos}")
        target = self._grid.get(key_to)
        if target:
            target.kill()
        del self._grid[key_from]
        piece.position = to_pos
        piece.move()
        self._grid[key_to] = piece

    def all_pieces(self) -> List[Piece]:
        return list(self._grid.values())

    def __str__(self) -> str:
        rows = []
        for r in range(8, 0, -1):
            row_pieces = []
            for c in range(1, 9):
                pos_num = PiecePosition.convert_row_column_to_position_number(r, c)
                piece = self._grid.get(pos_num)
                row_pieces.append(str(piece.icon) if piece else '.')
            rows.append('  '.join(row_pieces))
        return '\n'.join(rows)
