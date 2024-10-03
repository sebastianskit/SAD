import java.util.Observable;

@SuppressWarnings("deprecation")
public class Line extends Observable { // Extiende Observable para que otros (como Console) puedan observarla.
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
}
