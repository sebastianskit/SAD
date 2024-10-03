import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class EditableBufferedReader extends BufferedReader { // Extiende BufferedReader para soportar edición de línea.
    private Line line; // Objeto Line que será modificado.
    @SuppressWarnings("unused")
    private boolean insertMode; // Indica si estamos en modo de inserción (true por defecto).
    private boolean isWindows; // Verifica si estamos en un sistema Windows.

    public EditableBufferedReader(InputStreamReader in, Line line) { // Constructor que inicializa el lector y la línea
                                                                     // editable.
        super(in);
        this.line = line;
        this.insertMode = true; // El modo insertar está activado por defecto.
        this.isWindows = System.getProperty("os.name").toLowerCase().contains("win"); // Verifica si el sistema es
                                                                                      // Windows.
    }

    public void setRaw() throws IOException { // Método que pone el terminal en modo "raw" (sin procesar).
        if (isWindows) {
            // En Windows no se puede cambiar directamente al modo raw, por lo tanto se
            // muestra un mensaje.
            System.out.println("Modo RAW no es soportado directamente en Windows");
        } else {
            // En sistemas Unix, ejecuta un comando para poner el terminal en modo raw.
            Runtime.getRuntime().exec(new String[] { "/bin/sh", "-c", "stty raw -echo < /dev/tty" });
        }
    }

    public void unsetRaw() throws IOException { // Método para restaurar el terminal al modo normal.
        if (isWindows) {
            // En Windows no se requiere hacer nada, simplemente muestra un mensaje.
            System.out.println("Revirtiendo Modo RAW en Windows no es necesario");
        } else {
            // En sistemas Unix, ejecuta un comando para restaurar el modo normal del
            // terminal.
            Runtime.getRuntime().exec(new String[] { "/bin/sh", "-c", "stty cooked echo < /dev/tty" });
        }
    }

    @Override
    public String readLine() throws IOException { // Sobrescribe el método readLine para leer una línea editable.
        setRaw(); // Activa el modo raw para capturar cada tecla.
        int input;
        while ((input = read()) != '\r') { // Lee cada carácter hasta que se presiona Enter (detenido por '\r').
            handleInput(input); // Llama al método para manejar la entrada del usuario (caracteres, flechas,
                                // etc.).
        }
        unsetRaw(); // Restaura el terminal al modo normal después de capturar la entrada.
        return line.getContent(); // Retorna el contenido actual de la línea editada.
    }

    private void handleInput(int input) throws IOException { // Maneja las diferentes teclas que se pueden presionar.
        switch (input) {
            case 27: // El código 27 representa la tecla Escape, usada para las teclas de flecha.
                int next = read(); // Lee el siguiente carácter de la secuencia.
                if (next == 91) { // Si es una secuencia de control (como flechas).
                    handleArrowKeys(read()); // Llama al método para manejar las teclas de flecha.
                }
                break;
            case 127: // Código para Backspace en Unix.
            case 8: // Código para Backspace en Windows.
                line.deleteChar(); // Elimina el carácter en la posición actual del cursor.
                break;
            default:
                line.insertChar((char) input); // Si es un carácter normal, lo inserta en la línea.
        }
    }

    private void handleArrowKeys(int input) { // Maneja las teclas de flecha (izquierda, derecha, inicio, fin).
        switch (input) {
            case 68: // Flecha izquierda.
                line.moveCursorLeft(); // Mueve el cursor a la izquierda.
                break;
            case 67: // Flecha derecha.
                line.moveCursorRight(); // Mueve el cursor a la derecha.
                break;
            case 72: // Tecla Inicio (Home).
                line.moveCursorHome(); // Mueve el cursor al inicio de la línea.
                break;
            case 70: // Tecla Fin (End).
                line.moveCursorEnd(); // Mueve el cursor al final de la línea.
                break;
        }
    }
}
