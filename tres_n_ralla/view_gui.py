import tkinter as tk

class GameGUI:
    def __init__(self, master, game, on_button_click):
        self.master = master
        self.game = game
        self.on_button_click = on_button_click
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        self.create_widgets()

    def create_widgets(self):
        """Crea los botones para el tablero de juego"""
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.master, text=' ', width=10, height=3,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def update_view(self):
        """Actualiza la vista con el estado actual del tablero"""
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=self.game.board[row][col])

