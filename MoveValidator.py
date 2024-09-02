from ChessBoard import ChessBoard
from Move import Move


class MoveValidator:
    @staticmethod
    def is_valid_move(board: ChessBoard, move: Move) -> bool:
        # Implement basic move validation logic here
        # For now, we'll just check if the move is within the board
        end_row, end_col = move.end_pos
        return 0 <= end_row < 8 and 0 <= end_col < 8