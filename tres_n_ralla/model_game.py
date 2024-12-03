import random

class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]  # Tablero vacío
        self.current_player = 'X'  # El jugador humano será 'X'
    
    def play(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            if self.check_winner():
                return f"Player {self.current_player} wins!"
            elif self.check_draw():
                return "It's a draw!"
            self.toggle_player()
            return None  # Sin resultado, sigue el juego
        return "Invalid move"

    def toggle_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Verificar filas, columnas y diagonales
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False
    
    def check_draw(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))
    
    def available_moves(self):
        """Devuelve una lista de los movimientos disponibles"""
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']
    
    def minimax(self, depth, is_maximizing):
        """
        Implementación del algoritmo Minimax para la IA.
        """
        winner = None
        if self.check_winner():
            winner = self.current_player
        elif self.check_draw():
            winner = 'D'  # Empate

        if winner == 'X':
            return -1  # Si X gana, el jugador humano (X) gana
        elif winner == 'O':
            return 1  # Si O gana, la IA (O) gana
        elif winner == 'D':
            return 0  # Empate

        if is_maximizing:
            max_eval = float('-inf')
            for move in self.available_moves():
                self.board[move[0]][move[1]] = 'O'  # Hacer movimiento de IA
                eval = self.minimax(depth + 1, False)
                self.board[move[0]][move[1]] = ' '  # Deshacer movimiento
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for move in self.available_moves():
                self.board[move[0]][move[1]] = 'X'  # Hacer movimiento del jugador
                eval = self.minimax(depth + 1, True)
                self.board[move[0]][move[1]] = ' '  # Deshacer movimiento
                min_eval = min(min_eval, eval)
            return min_eval
    
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # 'X' empieza el juego

    def is_winner(self, player):
        """Comprobar si un jugador ha ganado"""
        # Comprobar filas, columnas y diagonales
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] == player:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def available_moves(self):
        """Retorna las casillas disponibles para jugar"""
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves

    def best_move(self):
        """Método para calcular la mejor jugada para la IA"""
        # Busca la primera casilla vacía (jugada aleatoria simple como ejemplo)
        available = self.available_moves()
        if available:
            return available[0]  # Solo selecciona el primer movimiento disponible
        return None

