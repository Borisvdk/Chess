from ChessPiece import ChessPiece

class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_board()
        self.selected_piece = None
        self.player_turn = "white"

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
        piece = self.board[start_row][start_col]
        if not piece:
            return False

        if self.board[end_row][end_col] and self.board[end_row][end_col].color == piece.color:
            return False

        # Add more specific move validation logic here for each piece type

        return True

    def move_piece(self, start_row, start_col, end_row, end_col):
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = None

    def calculate_valid_moves(self, start_row, start_col):
        piece = self.board[start_row][start_col]
        if piece.piece_type == "pawn":
            return [(start_row + 1, start_col), (start_row - 1, start_col)]
        # Add logic for other piece types
        return []