import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class TestReadLine {
    @SuppressWarnings("deprecation")
    public static void main(String[] args) {
        Line line = new Line();
        Console console = new Console();
        line.addObserver(console); // La consola observa los cambios en la línea

        BufferedReader reader = new EditableBufferedReader(new InputStreamReader(System.in), line);

        try {
            String result = reader.readLine();
            System.out.println("\nResultado final: " + result);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
