import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class EditableBufferedReader extends BufferedReader {
    private Line line;
    @SuppressWarnings("unused")
    private boolean insertMode;
    private boolean isWindows;

    public EditableBufferedReader(InputStreamReader in, Line line) {
        super(in);
        this.line = line;
        this.insertMode = true; // Modo insertar por defecto
        this.isWindows = System.getProperty("os.name").toLowerCase().contains("win");
    }

    public void setRaw() throws IOException {
        if (isWindows) {
            System.out.println("Modo RAW no es soportado directamente en Windows");
        } else {
            Runtime.getRuntime().exec(new String[] { "/bin/sh", "-c", "stty raw -echo < /dev/tty" });
        }
    }

    public void unsetRaw() throws IOException {
        if (isWindows) {
            // No se requiere 'unsetRaw' en Windows porque no cambiamos el modo.
            System.out.println("Revirtiendo Modo RAW en Windows no es necesario");
        } else {
            Runtime.getRuntime().exec(new String[] { "/bin/sh", "-c", "stty cooked echo < /dev/tty" });
        }
    }

    @Override
    public String readLine() throws IOException {
        setRaw();
        int input;
        while ((input = read()) != '\r') {
            handleInput(input);
        }
        unsetRaw();
        return line.getContent();
    }

    private void handleInput(int input) throws IOException {
        switch (input) {
            case 27: // Tecla de escape para flechas y secuencias especiales
                int next = read();
                if (next == 91) { // Secuencia de control de flechas
                    handleArrowKeys(read());
                }
                break;
            case 127: // Backspace
            case 8: // Backspace (Windows)
                line.deleteChar();
                break;
            default:
                line.insertChar((char) input);
        }
    }

    private void handleArrowKeys(int input) {
        switch (input) {
            case 68: // Flecha izquierda
                line.moveCursorLeft();
                break;
            case 67: // Flecha derecha
                line.moveCursorRight();
                break;
            case 72: // Inicio (Home)
                line.moveCursorHome();
                break;
            case 70: // Fin (End)
                line.moveCursorEnd();
                break;
        }
    }
}
