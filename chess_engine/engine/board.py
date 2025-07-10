"""
This module is responsible for managing the Board class,
 which handles the placement of pieces on the chessboard.
"""

from typing import Dict, Optional, List

from .piece.abstract import Piece
from .piece.position import PiecePosition, START_ROW_COL_INDEX, END_ROW_COL_INDEX
from .piece.color import ColorName
from .piece.creators import piece_creator, PieceName


class BoardError(Exception):
    """
    Exception raised for errors in the game state, such as invalid moves.
    """


class Board:
    """
    This class is responsible for managing the pieces on the chessboard and handling their
     movements, including special moves such as en passant.
    """
    def __init__(self):
        self._grid: Dict[int, Piece] = {}
        self.setup_initial_positions()

    def setup_initial_positions(self) -> None:
        """
        Sets up the initial positions of the pieces on the chessboard.

        This method clears the current board grid and places the pieces in their
        starting positions according to standard chess rules.
        """
        self._grid.clear()

        for col in range(START_ROW_COL_INDEX, END_ROW_COL_INDEX + 1):
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
        """
        Retrieves the piece at a given position on the chessboard.

        This method checks the board grid at the specified position and returns the piece
        located at that position. If there is no piece at the given position, it returns None.

        :param position: The position on the chessboard where the piece is to be retrieved.
                         This should be a `PiecePosition` object, which defines the location
                         of the piece on the board.
        :return: The piece at the specified position, or None if no piece exists at that position.
        """
        return self._grid.get(position.get_position_number())

    def move_piece(self, from_pos: PiecePosition, to_pos: PiecePosition) -> None:
        """
        Moves a piece from one position to another on the chessboard.

        This method retrieves the piece from the `from_pos` position, checks if there is
        a piece at the given position, and then moves it to the `to_pos` position on the
        chessboard. If a piece already exists at the `to_pos`, it is removed by calling
        its `kill()` method. After the move is made, the piece's position is updated
        and the board is updated with the new position.

        :param from_pos: The starting position of the piece to be moved, represented as a `PiecePosition`.
        :param to_pos: The target position where the piece is to be moved, also represented as a `PiecePosition`.

        :raises BoardError: If no piece exists at the `from_pos` position.

        :return: None
        """
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
        """
        Returns a list of all pieces currently on the chessboard.
        """
        return list(self._grid.values())

    def __str__(self) -> str:
        rows = []
        for r in range(END_ROW_COL_INDEX, START_ROW_COL_INDEX - 1, -1):
            row_pieces = []
            for c in range(START_ROW_COL_INDEX, END_ROW_COL_INDEX + 1):
                pos_num = PiecePosition.convert_row_column_to_position_number(r, c)
                piece = self._grid.get(pos_num)
                row_pieces.append(str(piece.icon) if piece else '.')
            rows.append('  '.join(row_pieces))
        return '\n'.join(rows)

    def serialize(self) -> List[Dict]:
        return [piece.serialize() for piece in self.all_pieces()]