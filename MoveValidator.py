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
        elif piece.piece_type == "pawn":
            return MoveValidator.is_valid_pawn_move(board, start_row, start_col, end_row, end_col)

        # Add logic for other pieces here
        return True

    @staticmethod
    def is_valid_king_move(start_row, start_col, end_row, end_col):
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        return max(row_diff, col_diff) == 1

    @staticmethod
    def is_valid_pawn_move(board, start_row, start_col, end_row, end_col):
        piece = board[start_row][start_col]
        direction = -1 if piece.color == "white" else 1
        row_diff = end_row - start_row
        col_diff = abs(end_col - start_col)

        # Regular move (1 square forward)
        if col_diff == 0 and row_diff == direction and not board[end_row][end_col]:
            return True

        # First move (option to move 2 squares)
        if col_diff == 0 and row_diff == 2 * direction and not board[end_row][end_col] and not \
        board[start_row + direction][start_col]:
            return (piece.color == "white" and start_row == 6) or (piece.color == "black" and start_row == 1)

        # Capture move (diagonally)
        if col_diff == 1 and row_diff == direction and board[end_row][end_col] and board[end_row][
            end_col].color != piece.color:
            return True

        return False


    @staticmethod
    def calculate_valid_moves(board, row, col):
        piece = board[row][col]
        if piece.piece_type == "king":
            return MoveValidator.calculate_king_moves(board, row, col)
        if piece.piece_type == "pawn":
            return MoveValidator.calculate_pawn_moves(board, row, col)
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

    @staticmethod
    def calculate_pawn_moves(board, row, col):
        piece = board[row][col]
        valid_moves = []
        direction = -1 if piece.color == "white" else 1

        # Move forward one square
        new_row = row + direction
        if 0 <= new_row < 8 and not board[new_row][col]:
            valid_moves.append((new_row, col))

            # First move: option to move two squares
            if (piece.color == "white" and row == 6) or (piece.color == "black" and row == 1):
                new_row = row + 2 * direction
                if 0 <= new_row < 8 and not board[new_row][col]:
                    valid_moves.append((new_row, col))

        # Capture moves (diagonally)
        for col_offset in [-1, 1]:
            new_col = col + col_offset
            new_row = row + direction
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] and board[new_row][new_col].color != piece.color:
                    valid_moves.append((new_row, new_col))

        return valid_moves