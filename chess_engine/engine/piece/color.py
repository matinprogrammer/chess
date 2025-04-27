from enum import Enum


__all__ = ["PieceColor", "ColorName", "PieceColorError"]


class PieceColorError(Exception):
    pass


class ColorName(Enum):
    WHITE = "white"
    BLACK = "black"


class PieceColor:
    def __init__(self, color: ColorName) -> None:
        self.color = color

    @property
    def color(self) -> ColorName:
        return self._color

    @color.setter
    def color(self, value: ColorName) -> None:
        if not isinstance(value, ColorName):
            raise PieceColorError(f"Color must be a string or Color enum, got {type(value)}")
        self._color = value

    @color.deleter
    def color(self) -> None:
        raise PieceColorError("Color cannot be deleted")

    def __str__(self) -> str:
        return self._color.value

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} color={self._color}>"