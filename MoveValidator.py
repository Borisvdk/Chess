class MoveValidator:
    @staticmethod
    def is_valid_move(board, start_row, start_col, end_row, end_col):
        piece = board[start_row][start_col]
        if not piece:
            return False

        if board[end_row][end_col] and board[end_row][end_col].color == piece.color:
            return False

        if piece.piece_type == "king":
            return MoveValidator.is_valid_king_move(start_row, start_col, end_row, end_col)


        # Add logic for other pieces here
        return True

    @staticmethod
    def is_valid_king_move(start_row, start_col, end_row, end_col):
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        return max(row_diff, col_diff) == 1

    @staticmethod
    def calculate_valid_moves(board, row, col):
        piece = board[row][col]
        if piece.piece_type == "king":
            return MoveValidator.calculate_king_moves(board, row, col)
        # Add methods for other pieces
        return []

    @staticmethod
    def calculate_king_moves(board, row, col):
        valid_moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_row, new_col = row + i, col + j
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if not board[new_row][new_col] or board[new_row][new_col].color != board[row][col].color:
                        valid_moves.append((new_row, new_col))
        return valid_moves