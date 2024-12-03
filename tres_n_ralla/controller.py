from model_game import Game
from view_gui import GameGUI
import tkinter as tk
from tkinter import messagebox, simpledialog

class GameController:
    def __init__(self, master):
        # Primero pedimos el modo de juego antes de crear el tablero
        self.mode = self.ask_game_mode()

        # Iniciamos el modelo del juego
        self.game = Game()

        # Luego pasamos al siguiente paso, que es crear la vista (GUI)
        self.view = GameGUI(master, self.game, self.on_button_click)

    def ask_game_mode(self):
        """Preguntar al usuario si quiere jugar contra otro jugador o contra la IA"""
        mode = simpledialog.askstring("Game Mode", "Enter game mode:\nplayer_vs_player\nplayer_vs_ai")
        
        # Validamos la entrada, y si es incorrecta, asignamos el modo por defecto
        if mode not in ['player_vs_player', 'player_vs_ai']:
            mode = 'player_vs_player'
        return mode

    def on_button_click(self, row, col):
        """Maneja el clic en el tablero (jugador hace un movimiento)"""
        if self.game.board[row][col] != ' ':
            return  # Si la casilla ya está ocupada, no hace nada

        result = self.game.play(row, col)  # Jugar el turno del jugador

        if result:
            messagebox.showinfo("Game Over", result)
            self.view.master.quit()  # Cierra la ventana cuando termina el juego
        else:
            if self.mode == 'player_vs_ai' and self.game.current_player == 'O':  # Si es el turno de la IA
                self.ai_move()  # La IA realiza su movimiento
            else:
                self.view.update_view()  # Actualiza la vista si el juego continúa


    def ai_move(self):
        """Manejo del movimiento de la IA"""
        # Muestra un mensaje indicando que la IA está haciendo su jugada
        messagebox.showinfo("IA Turn", "La IA está haciendo su jugada...")

        # Hace el movimiento de la IA obteniendo el mejor movimiento
        best_move = self.game.best_move()
    
        # Verifica si se obtuvo un movimiento válido
        if best_move:
            row, col = best_move
            self.game.play(row, col)  # Realiza el movimiento en el tablero
            self.view.update_view()    # Actualiza la vista con el movimiento de la IA

        # Después de hacer la jugada, muestra el resultado o continua el juego
        result = self.game.check_winner()
        if result:
            messagebox.showinfo("Game Over", result)
            self.view.master.quit()  # Cierra la ventana cuando termina el juego
        else:
            messagebox.showinfo("Game Over", "¡Empate!")
        self.view.master.quit()  # Cierra la ventana cuando termina el juego
