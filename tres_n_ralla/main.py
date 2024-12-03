from controller import GameController
import tkinter as tk

if __name__ == "__main__":
    # Crea la ventana raíz de Tkinter
    root = tk.Tk()
    
    # Llamamos al controlador para que obtenga el modo de juego antes de iniciar la ventana
    controller = GameController(root)
    
    # Inicia la ventana principal de Tkinter
    root.mainloop()  # Esto inicia el bucle principal de la interfaz gráfica
