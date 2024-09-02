import tkinter as tk
from PIL import Image, ImageTk
import os
import logging

logging.basicConfig(level=logging.DEBUG)


class ChessPiece:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type


class ChessBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.selected_piece = None
        self.player_turn = "white"

        self.board_size = 800  # Adjust this value to change the overall board size
        self.cell_size = self.board_size // 8

        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_board()

        self.images = {}
        self.load_images()
        self.create_board_gui()

    def initialize_board(self):
        logging.debug("Initializing board")
        # Initialize pawns
        for col in range(8):
            self.board[1][col] = ChessPiece("white", "pawn")
            self.board[6][col] = ChessPiece("black", "pawn")

        # Initialize other pieces
        piece_order = ["rook", "knight", "bishop", "queen", "king", "bishop", "knight", "rook"]
        for col in range(8):
            self.board[0][col] = ChessPiece("white", piece_order[col])
            self.board[7][col] = ChessPiece("black", piece_order[col])

    def create_board_gui(self):
        self.canvas = tk.Canvas(self.root, width=self.board_size, height=self.board_size)
        self.canvas.pack()

        for row in range(8):
            for col in range(8):
                color = "white" if (row + col) % 2 == 0 else "gray"
                x1, y1 = col * self.cell_size, (7 - row) * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.update_board_gui()

    def update_board_gui(self):
        self.canvas.delete("piece")
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    image_key = f"{piece.color}_{piece.piece_type}"
                    if image_key in self.images:
                        x = col * self.cell_size + self.cell_size // 2
                        y = (7 - row) * self.cell_size + self.cell_size // 2
                        self.canvas.create_image(x, y, image=self.images[image_key], tags="piece")

    def load_images(self):
        piece_types = ["pawn", "rook", "knight", "bishop", "queen", "king"]
        colors = ["white", "black"]
        for color in colors:
            for piece_type in piece_types:
                filename = f"chess_pieces/{color}_{piece_type}.png"
                if os.path.exists(filename):
                    img = Image.open(filename)
                    img = img.resize((self.cell_size, self.cell_size), Image.LANCZOS)
                    self.images[f"{color}_{piece_type}"] = ImageTk.PhotoImage(img)

    def on_canvas_click(self, event):
        col = event.x // self.cell_size
        row = 7 - (event.y // self.cell_size)

        if self.selected_piece is None:
            if self.board[row][col] and self.board[row][col].color == self.player_turn:
                self.selected_piece = (row, col)
                self.highlight_square(row, col)
        else:
            start_row, start_col = self.selected_piece
            if self.is_valid_move(start_row, start_col, row, col):
                self.move_piece(start_row, start_col, row, col)
                self.player_turn = "black" if self.player_turn == "white" else "white"
            self.clear_highlights()
            self.selected_piece = None

    def highlight_square(self, row, col):
        x1, y1 = col * self.cell_size, (7 - row) * self.cell_size
        x2, y2 = x1 + self.cell_size, y1 + self.cell_size
        self.canvas.create_rectangle(x1, y1, x2, y2, outline="yellow", width=3, tags="highlight")

    def clear_highlights(self):
        self.canvas.delete("highlight")

    def calculate_valid_moves(self, start_row, start_col, piece_type):
        if piece_type == "pawn":
            return [(start_row + 1, start_col), (start_row - 1, start_col)]

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
        self.update_board_gui()


if __name__ == "__main__":
    root = tk.Tk()
    game = ChessBoard(root)
    root.mainloop()