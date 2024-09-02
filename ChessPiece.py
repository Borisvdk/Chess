from Color import Color
from PieceType import PieceType


class ChessPiece:
    def __init__(self, color: Color, piece_type: PieceType):
        self.color = color
        self.piece_type = piece_type

    def __str__(self):
        return f"{self.color.name} {self.piece_type.name}"