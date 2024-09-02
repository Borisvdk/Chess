from ChessPiece import ChessPiece
from MoveValidator import MoveValidator


class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_board()
        self.selected_piece = None
        self.player_turn = "white"
        self.white_king_pos = (0, 4)
        self.black_king_pos = (7, 4)

    def initialize_board(self):
        # Initialize pawns
        for col in range(8):
            self.board[1][col] = ChessPiece("white", "pawn")
            self.board[6][col] = ChessPiece("black", "pawn")

        # Initialize other pieces
        piece_order = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
        for col in range(8):
            self.board[0][col] = ChessPiece("white", piece_order[col])
            self.board[7][col] = ChessPiece("black", piece_order[col])

    def is_valid_move(self, start_row, start_col, end_row, end_col):
        return MoveValidator.is_valid_move(self.board, start_row, start_col, end_row, end_col)

    def calculate_valid_moves(self, row, col):
        return MoveValidator.calculate_valid_moves(self.board, row, col)

    def move_piece(self, start_row, start_col, end_row, end_col):
        piece = self.board[start_row][start_col]
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = None

        if piece.piece_type == "king":
            if piece.color == "white":
                self.white_king_pos = (end_row, end_col)
            else:
                self.black_king_pos = (end_row, end_col)