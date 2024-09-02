import tkinter as tk
from ChessBoard import ChessBoard
from ChessGUI import ChessGUI

def main():
    root = tk.Tk()
    chess_game = ChessBoard()
    chess_gui = ChessGUI(root, chess_game)
    root.mainloop()

if __name__ == "__main__":
    main()