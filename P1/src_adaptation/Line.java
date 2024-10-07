import java.util.Observable;
import java.util.Observer;

@SuppressWarnings("deprecation")
public class Line extends Observable implements Observer { // Extiende Observable para que otros (como Console) puedan
                                                           // observarla.
    private StringBuilder content; // Contiene el contenido de la línea.
    private int cursorPosition; // Posición actual del cursor en la línea.

    public Line() { // Constructor que inicializa el contenido vacío y el cursor en posición 0.
        this.content = new StringBuilder();
        this.cursorPosition = 0;
    }

    public String getContent() { // Devuelve el contenido actual de la línea.
        return content.toString();
    }

    public int getCursorPosition() { // Devuelve la posición actual del cursor.
        return cursorPosition;
    }

    public void insertChar(char ch) { // Inserta un carácter en la posición actual del cursor.
        content.insert(cursorPosition, ch); // Inserta el carácter en la posición indicada.
        cursorPosition++; // Mueve el cursor a la derecha.
        setChanged(); // Indica que el estado ha cambiado.
        notifyObservers(); // Notifica a los observadores (Console) para que actualicen la vista.
    }

    public void deleteChar() { // Elimina el carácter en la posición anterior al cursor.
        if (cursorPosition > 0) {
            content.deleteCharAt(cursorPosition - 1); // Elimina el carácter a la izquierda del cursor.
            cursorPosition--; // Mueve el cursor una posición a la izquierda.
            setChanged(); // Indica que el estado ha cambiado.
            notifyObservers(); // Notifica a los observadores para que actualicen la consola.
        }
    }

    public void moveCursorLeft() { // Mueve el cursor una posición a la izquierda.
        if (cursorPosition > 0) {
            cursorPosition--;
            setChanged();
            notifyObservers(); // Notifica a los observadores del cambio de posición del cursor.
        }
    }

    public void moveCursorRight() { // Mueve el cursor una posición a la derecha.
        if (cursorPosition < content.length()) {
            cursorPosition++;
            setChanged();
            notifyObservers();
        }
    }

    public void moveCursorHome() { // Mueve el cursor al inicio de la línea.
        cursorPosition = 0;
        setChanged();
        notifyObservers();
    }

    public void moveCursorEnd() { // Mueve el cursor al final de la línea.
        cursorPosition = content.length();
        setChanged();
        notifyObservers();
    }

    public void reset() { // Resetea la línea (borra el contenido y mueve el cursor al inicio).
        content.setLength(0);
        cursorPosition = 0;
        setChanged();
        notifyObservers(); // Notifica a los observadores que la línea ha sido reseteada.
    }

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
