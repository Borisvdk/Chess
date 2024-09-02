import tkinter as tk
from PIL import Image, ImageTk
import os
from ChessBoard import ChessBoard
from ChessPiece import ChessPiece

class ChessGUI:
    def __init__(self, root, chess_game):
        self.root = root
        self.root.title("Chess Game")
        self.chess_game = chess_game

        self.board_size = 800
        self.cell_size = self.board_size // 8

        self.images = {}
        self.load_images()
        self.create_board_gui()

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
                piece = self.chess_game.board[row][col]
                if piece:
                    image_key = f"{piece.color}_{piece.piece_type}"
                    if image_key in self.images:
                        x = col * self.cell_size + self.cell_size // 2
                        y = (7 - row) * self.cell_size + self.cell_size // 2
                        self.canvas.create_image(x, y, image=self.images[image_key], tags="piece")

    def on_canvas_click(self, event):
        col = event.x // self.cell_size
        row = 7 - (event.y // self.cell_size)

        if self.chess_game.selected_piece is None:
            if self.chess_game.board[row][col] and self.chess_game.board[row][col].color == self.chess_game.player_turn:
                self.chess_game.selected_piece = (row, col)
                self.highlight_square(row, col)
        else:
            start_row, start_col = self.chess_game.selected_piece
            if self.chess_game.is_valid_move(start_row, start_col, row, col):
                self.chess_game.move_piece(start_row, start_col, row, col)
                self.chess_game.player_turn = "black" if self.chess_game.player_turn == "white" else "white"
            self.clear_highlights()
            self.chess_game.selected_piece = None
        self.update_board_gui()

    def highlight_square(self, row, col):
        x1, y1 = col * self.cell_size, (7 - row) * self.cell_size
        x2, y2 = x1 + self.cell_size, y1 + self.cell_size
        self.canvas.create_rectangle(x1, y1, x2, y2, outline="yellow", width=3, tags="highlight")

    def clear_highlights(self):
        self.canvas.delete("highlight")