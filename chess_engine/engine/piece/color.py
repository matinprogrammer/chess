"""
Module for managing chess piece colors and related operations.

This module defines the ColorName Enum for piece colors (white and black),
the PieceColor class for handling a piece's color with validation,
and the PieceColorError exception for error handling.
"""
from enum import Enum

__all__ = ["PieceColor", "ColorName", "PieceColorError"]


class PieceColorError(Exception):
    """
    Exception raised for invalid piece color operations.
    """


class ColorName(Enum):
    """
    Enum for chess piece colors: WHITE and BLACK.
    """
    WHITE = "white"
    BLACK = "black"


class PieceColor:
    """
    Class for managing a chess piece's color.

    Ensures that the color is either WHITE or BLACK and provides validation.
    """

    def __init__(self, color: ColorName) -> None:
        self.color = color

    @property
    def color(self) -> ColorName:
        """
        Gets the current color of the chess piece.

        :return: The color as a ColorName Enum.
        """
        return self._color

    @color.setter
    def color(self, value: ColorName) -> None:
        """
        Sets the color of the chess piece.

        :param value: A ColorName Enum value (WHITE or BLACK).
        :raises PieceColorError: If the color is invalid.
        """
        if not isinstance(value, ColorName):
            raise PieceColorError(f"Color must be an instance of ColorName enum, got {type(value)}.")
        self._color = value

    @color.deleter
    def color(self) -> None:
        """
        Prevents the deletion of the color attribute.

        :raises PieceColorError: Always raises an error.
        """
        raise PieceColorError("Color cannot be deleted")

    def __str__(self) -> str:
        return self._color.value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.color=})"
