"""
Chessboard Positioning and Movement System

This module provides classes and functions to represent chessboard positions,
validate file and rank inputs, and generate possible movements for chess pieces.
It defines classes for both the columns (files) and positions of pieces on the board.
Additionally, it includes methods to move chess pieces and convert between position formats.

Classes:
    - ChessFile: Represents a chess file (column), either as a letter ('a'-'h') or a number (1-8).
    - PiecePosition: Represents the position of a piece on the chessboard, consisting of a row (1-8) and a column (file).

Exceptions:
    - ChessFileError: Raised when there is an invalid file (column) input.
    - PiecePositionError: Raised when there is an invalid position (row or column) input.

Constants:
    - START_ROW_COL_INDEX: The starting index for rows and columns (1).
    - END_ROW_COL_INDEX: The ending index for rows and columns (8).
    - START_BOARD_INDEX: The starting index for the board's positions (1).
    - END_BOARD_INDEX: The ending index for the board's positions (64).
"""
from typing import Tuple, Optional

__all__ = ["ChessFile", "PiecePosition", "ChessFileError", "PiecePositionError"]

START_ROW_COL_INDEX = 1
END_ROW_COL_INDEX = 8
START_BOARD_INDEX = 1
END_BOARD_INDEX = 64


class PiecePositionError(Exception):
    """
    Exception raised for errors related to piece positions.

    This error is raised when a piece's row or column is out of valid range (1-8 for row, 'a'-'h' or 1-8 for column).
    """


class ChessFileError(Exception):
    """
    Exception raised for errors related to chess file (column) input.

    This error is raised when the input value for a chess file is invalid. Valid inputs are
    letters ('a'-'h') or numbers (1-8).
    """


class ChessFile:
    """
    A class to represent a chess file (column) on the chessboard.

    The file can be represented as a letter ('a' to 'h') or a number (1 to 8).
    This class ensures that the input is valid and provides properties to access the file's letter and number.

    Attributes:
        index (int): The numerical representation of the file (1-8).
    """
    _letters = "abcdefgh"

    def __init__(self, value: str | int):
        """
        Initializes the ChessFile with either a letter (a-h) or a number (1-8).

        Args:
            value (str | int): The file letter (a-h) or file number (1-8).

        Raises:
            ChessFileError: If the value is not a valid letter or number.
        """
        if isinstance(value, str):
            value = value.lower()
            if value not in self._letters:
                raise ChessFileError("Invalid file letter. Must be between 'a' and 'h'.")
            self.index = self._letters.index(value) + 1
        elif isinstance(value, int):
            if not (START_ROW_COL_INDEX <= value <= END_ROW_COL_INDEX):     # pylint: disable=superfluous-parens
                raise ChessFileError(
                    f"Invalid file number. Must be between {START_ROW_COL_INDEX} and {END_ROW_COL_INDEX}."
                )
            self.index = value
        else:
            raise ChessFileError(
                f"File must be a letter (a-h) or a number ({START_ROW_COL_INDEX}-{END_ROW_COL_INDEX})."
            )

    @property
    def letter(self) -> str:
        """
        Returns the letter representation of the file (a-h).

        Returns:
            str: The letter of the chess file.
        """
        return self._letters[self.index - 1]

    @property
    def number(self) -> int:
        """
        Returns the number representation of the file (1-8).

        Returns:
            int: The number of the chess file.
        """
        return self.index

    def __str__(self):
        return self.letter

    def __repr__(self):
        return f"ChessFile('{self.letter}')"

    def __int__(self):
        return self.index

    def __eq__(self, other):
        if isinstance(other, ChessFile):
            return self.index == other.index
        return NotImplemented


class PiecePosition:
    """
       A class to represent a piece's position on the chessboard using row and column.

       The row is an integer between 1 and 8, and the column can be represented either
       by a letter (a-h) or a number (1-8). This class validates and provides utility
       methods for moving pieces and converting between different representations of position.

       Attributes:
           row (int): The row of the piece (1-8).
           column (ChessFile): The column of the piece represented as a ChessFile object.
       """

    def __init__(self, row: int, column: int | str):
        """
        Initializes the PiecePosition with a row and column.

        Args:
            row (int): The row of the piece (1-8).
            column (int | str): The column of the piece, either a letter ('a'-'h') or a number (1-8).

        Raises:
            PiecePositionError: If the row or column is not valid.
        """
        self.row = row
        self.column = column

    @property
    def row(self):
        """
        Returns the row of the piece (1-8).
        """
        return self._row

    @row.setter
    def row(self, value: int):
        """
        Sets the row of the piece, ensuring it is between 1 and 8.
        """
        if not PiecePosition.validate_axis(value):
            raise PiecePositionError("piece row must be between 1 and 8 inclusive.")
        self._row = value

    @row.deleter
    def row(self):
        """
        always rais error
        """
        raise PiecePositionError("piece row cannot be deleted")

    @property
    def column(self):
        """
        Returns the column of the piece as a ChessFile object.
        """
        return self._column

    @column.setter
    def column(self, value: int | str):
        """
        Sets the column of the piece using the ChessFile class.
        """
        self._column = ChessFile(value)

    @column.deleter
    def column(self):
        """
        always rais error
        """
        raise PiecePositionError("piece column cannot be deleted")

    @property
    def column_number(self) -> int:
        """
        Returns the column number (1-8) from the column.
        """
        return self.column.number

    def get_row_column(self) -> Tuple[int, int]:
        """
        Returns the row and column as a tuple.
        """
        return self.row, self.column.number

    def get_position_number(self) -> int:
        """
        Converts the current position to a position number (1-64).

        Returns:
            int: The position number between 1 and 64.
        """
        return PiecePosition.convert_row_column_to_position_number(self.row, self.column.number)

    @staticmethod
    def validate_axis(value: int) -> bool:
        """
        Validates that a value is between 1 and 8 inclusive.

        Args:
            value (int): The value to validate.

        Returns:
            bool: True if the value is between 1 and 8, otherwise False.
        """
        return START_ROW_COL_INDEX <= value <= END_ROW_COL_INDEX

    @staticmethod
    def validate_position_number(value: int) -> bool:
        """
        Validates that a position number is between 1 and 64 inclusive.

        Args:
            value (int): The position number to validate.

        Returns:
            bool: True if the position number is between 1 and 64, otherwise False.
        """
        return START_BOARD_INDEX <= value <= END_BOARD_INDEX

    @staticmethod
    def convert_row_column_to_position_number(row: int, column: int) -> int:
        """
        Converts row and column values to a position number (1-64).

        Args:
            row (int): The row of the piece (1-8).
            column (int): The column of the piece (1-8).

        Returns:
            int: The position number between 1 and 64.
        """
        if not PiecePosition.validate_axis(row):
            raise PiecePositionError("piece row index must be between and equal 1 and 8")
        if not PiecePosition.validate_axis(column):
            raise PiecePositionError("piece column index must be between and equal 1 and 8")
        return (row - 1) * 8 + column

    @staticmethod
    def convert_position_number_to_row_column(position_number: int) -> Tuple[int, int]:
        """
        Converts a position number to row and column values.

        Args:
            position_number (int): The position number between 1 and 64.

        Returns:
            Tuple[int, int]: The row and column values.
        """
        if not PiecePosition.validate_position_number(position_number):
            raise PiecePositionError("piece position number must be between and equal 1 and 64")
        return (position_number - 1) // 8 + 1, (position_number - 1) % 8 + 1

    @classmethod
    def create_position_from_position_number(cls, position_number: int) -> 'PiecePosition':
        """
        Create a PiecePosition from a position number.

        This method takes a position number (between 1 and 64) and uses the conversion method to calculate the
        corresponding row and column, and then returns a new PiecePosition object based on these values.

        Args:
            position_number (int): The position number between 1 and 64, which will be converted into a PiecePosition.

        Returns:
            PiecePosition: A PiecePosition object representing the position on the chessboard.
        """
        return cls(*cls.convert_position_number_to_row_column(position_number))

    def __eq__(self, other):
        if isinstance(other, PiecePosition):
            return self.row == other.row and self.column_number == other.column_number
        return NotImplemented

    @classmethod
    def move_up(cls, pos: 'PiecePosition'):
        """
        Generate all possible positions for moving the piece up.
        """
        for r in range(pos.row + 1, 9):
            yield cls(r, pos.column.number)

    @classmethod
    def move_down(cls, pos: 'PiecePosition'):
        """
        Generate all possible positions for moving the piece down.
        """
        for r in range(pos.row - 1, 0, -1):
            yield cls(r, pos.column.number)

    @classmethod
    def move_right(cls, pos: 'PiecePosition'):
        """
        Generate all possible positions for moving the piece right.
        """
        for c in range(pos.column.number + 1, 9):
            yield cls(pos.row, c)

    @classmethod
    def move_left(cls, pos: 'PiecePosition'):
        """
        Generate all possible positions for moving the piece left.
        """
        for c in range(pos.column.number - 1, 0, -1):
            yield cls(pos.row, c)

    @classmethod
    def move_up_right(cls, pos: 'PiecePosition'):
        """
        Generate all possible positions for moving the piece diagonally up-right.
        """
        r, c = pos.row + 1, pos.column.number + 1
        while r <= END_ROW_COL_INDEX and c <= END_ROW_COL_INDEX:
            yield cls(r, c)
            r += 1
            c += 1

    @classmethod
    def move_up_left(cls, pos: 'PiecePosition'):
        """
        Generate all possible positions for moving the piece diagonally up-left.
        """
        r, c = pos.row + 1, pos.column.number - 1
        while r <= END_ROW_COL_INDEX and c >= START_ROW_COL_INDEX:
            yield cls(r, c)
            r += 1
            c -= 1

    @classmethod
    def move_down_right(cls, pos: 'PiecePosition'):
        """
        Generate all possible positions for moving the piece diagonally down-right.
        """
        r, c = pos.row - 1, pos.column.number + 1
        while r >= START_ROW_COL_INDEX and c <= END_ROW_COL_INDEX:
            yield cls(r, c)
            r -= 1
            c += 1

    @classmethod
    def move_down_left(cls, pos: 'PiecePosition'):
        """
        Generate all possible positions for moving the piece diagonally down-left.
        """
        r, c = pos.row - 1, pos.column.number - 1
        while r >= START_ROW_COL_INDEX and c >= START_ROW_COL_INDEX:
            yield cls(r, c)
            r -= 1
            c -= 1

    @classmethod
    def offset(cls, pos: 'PiecePosition', offset: Tuple[int, int]) -> Optional['PiecePosition']:
        """
        Calculate a new position by applying an offset to the current position.

        This method applies a shift in the row and column to the current position and checks whether the new position
        lies within the boundaries of the chessboard. If the new position is valid, it creates and returns a new
        PiecePosition object; otherwise, it returns None.

        Args:
            pos (PiecePosition): The current position of the piece on the chessboard.
            offset (Tuple[int, int]): The shift (offset) in row and column as a tuple of two integers.
                                      The first value is the row offset (dr), and the second is the column offset (dc).

        Returns:
            Optional[PiecePosition]: If the new position is valid, it returns a new PiecePosition object,
                                      otherwise, it returns None.
        """
        dr, dc = offset
        new_row = pos.row + dr
        new_col = pos.column.number + dc
        if START_ROW_COL_INDEX <= new_row <= END_ROW_COL_INDEX and START_ROW_COL_INDEX <= new_col <= END_ROW_COL_INDEX:
            return cls(new_row, new_col)
        return None

    def __hash__(self):
        return hash((self.row, self.column.number))

    def __str__(self) -> str:
        return f"{self.column.letter}{self.row}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.row=}, {self.column=})"
