from ChessPiece import ChessPiece

class Move:
    def __init__(self, start_pos: tuple, end_pos: tuple, piece: ChessPiece):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.piece = piece

    def __str__(self):
        return f"{self.piece} from {self.start_pos} to {self.end_pos}"