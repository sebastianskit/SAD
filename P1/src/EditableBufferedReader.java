import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class EditableBufferedReader extends BufferedReader {

    public EditableBufferedReader(InputStreamReader in) {
        super(in);
    }

    public void setRaw() throws IOException {
        
        Runtime.getRuntime().exec(new String[] { "/bin/sh", "-c", "stty raw -echo </dev/tty" });
    }

    public void unsetRaw() throws IOException {
        
        Runtime.getRuntime().exec(new String[] { "/bin/sh", "-c", "stty cooked echo </dev/tty" });
    }

    public int read() throws IOException {
        // Implementar la lectura de caràcters i seqüències d'escape
        int ch = super.read();
        if (ch == 27) { // Si detectem una seqüència d'escape (ESC)
            // Aquí s'hauria de gestionar la lectura de les tecles especials
            return super.read(); // simplificat per a l'exemple
        }
        return ch;
    }

    public String readLine() throws IOException {
        setRaw(); // Posar en mode raw
        StringBuilder sb = new StringBuilder();
        int ch;
        while ((ch = read()) != '\n') { // llegim fins a trobar un salt de línia
            sb.append((char) ch);
        }
        unsetRaw(); // Tornar al mode cooked
        return sb.toString();
    }
}
