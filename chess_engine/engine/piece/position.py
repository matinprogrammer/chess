from typing import Tuple, Self


class PiecePositionError(Exception):
    pass


class ChessFileError(Exception):
    pass


class ChessFile:
    _letters = "abcdefgh"

    def __init__(self, value: str | int):
        if isinstance(value, str):
            value = value.lower()
            if value not in self._letters:
                raise ChessFileError("Invalid file letter. Must be between 'a' and 'h'.")
            self.index = self._letters.index(value) + 1
        elif isinstance(value, int):
            if not (1 <= value <= 8):
                raise ChessFileError("Invalid file number. Must be between 1 and 8.")
            self.index = value
        else:
            raise ChessFileError("File must be a letter (a-h) or a number (1-8).")

    @property
    def letter(self) -> str:
        return self._letters[self.index - 1]

    @property
    def number(self) -> int:
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
    def __init__(self, row: int, column: int | str):
        self.row = row
        self.column= column

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, value: int):
        if not PiecePosition.validate_axis(value):
            raise PiecePositionError("piece row must be between 1 and 8 inclusive.")
        self._row = value

    @row.deleter
    def row(self):
        raise PiecePositionError("piece row cannot be deleted")

    @property
    def column(self):
        return self._column

    @column.setter
    def column(self, value: int | str):
        self._column = ChessFile(value)

    @column.deleter
    def column(self):
        raise PiecePositionError("piece column cannot be deleted")

    @property
    def column_number(self) -> int:
        return self.column.number

    def get_row_column(self) -> Tuple[int, int]:
        return self.row, self.column.number

    def get_position_number(self) -> int:
        return PiecePosition.convert_row_column_to_position_number(self.row, self.column.number)

    @staticmethod
    def validate_axis(value: int) -> bool:
        return 1 <= value <= 8

    @staticmethod
    def validate_position_number(value: int) -> bool:
        return 1 <= value <= 64

    @staticmethod
    def convert_row_column_to_position_number(row: int, column: int) -> int:
        if not PiecePosition.validate_axis(row):
            raise PiecePositionError("piece row index must be between and equal 1 and 8")
        if not PiecePosition.validate_axis(column):
            raise PiecePositionError("piece column index must be between and equal 1 and 8")
        return (row - 1) * 8 + column

    @staticmethod
    def convert_position_number_to_row_column(position_number: int) -> Tuple[int, int]:
        if not PiecePosition.validate_position_number(position_number):
            raise PiecePositionError("piece position number must be between and equal 1 and 64")
        return (position_number - 1) // 8 + 1, (position_number - 1) % 8 + 1

    @classmethod
    def create_position_from_position_number(cls, position_number: int) -> Self:
        return cls(*cls.convert_position_number_to_row_column(position_number))

    def __str__(self) -> str:
        return f"{self.column.letter}{self.row}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.row=}, {self.column=})"

    def __eq__(self, other):
        if isinstance(other, PiecePosition):
            return self.row == other.row and self.column_number == other.column_number
        return NotImplemented
