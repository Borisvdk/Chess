from ChessBoard import ChessBoard
from Color import Color
from Move import Move
from MoveValidator import MoveValidator


class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.current_player = Color.WHITE
        self.move_validator = MoveValidator()

    def make_move(self, start_pos: tuple, end_pos: tuple) -> bool:
        piece = self.board.get_piece(*start_pos)
        if piece and piece.color == self.current_player:
            move = Move(start_pos, end_pos, piece)
            if self.move_validator.is_valid_move(self.board, move):
                self.board.move_piece(move)
                self.current_player = Color.BLACK if self.current_player == Color.WHITE else Color.WHITE
                return True
        return False

    def __str__(self):
        return str(self.board)