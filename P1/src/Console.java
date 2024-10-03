import java.util.Observable;
import java.util.Observer;

@SuppressWarnings("deprecation")
public class Console implements Observer { // Implementa la interfaz Observer, es decir, observará los cambios en los
                                           // objetos observables.

    @Override
    public void update(Observable o, Object arg) { // Método que se llama cuando el objeto observado (Line) cambia.
        if (o instanceof Line) { // Verifica si el objeto observado es de tipo Line.
            Line line = (Line) o; // Convierte el observable a tipo Line.
            render(line); // Llama al método render para mostrar la línea en consola.
        }
    }

    public void render(Line line) { // Renderiza (muestra) el contenido de la línea en la consola.
        clearConsole(); // Limpia la consola antes de mostrar el contenido actualizado.
        System.out.print(line.getContent()); // Imprime el contenido actual de la línea.
        moveCursorToPosition(line.getCursorPosition()); // Mueve el cursor a la posición correcta.
    }

    public void clearConsole() { // Método que limpia la consola usando códigos ANSI.
        System.out.print("\033[H\033[2J"); // Código ANSI para limpiar la consola y mover el cursor al inicio.
        System.out.flush(); // Fuerza la limpieza de la consola.
    }

    private void moveCursorToPosition(int position) { // Mueve el cursor a una posición específica en la línea.
        System.out.print("\033[" + (position + 1) + "G"); // Código ANSI para mover el cursor a la posición deseada.
    }
}
