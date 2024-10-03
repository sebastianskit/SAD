import java.io.IOException;
import java.io.InputStreamReader;
import java.io.BufferedReader;

public class TestReadLine { // Clase principal para probar la funcionalidad de lectura y edición de la
    // línea.
    @SuppressWarnings("deprecation")
    public static void main(String[] args) {
        Line line = new Line(); // Crea una nueva línea que será editada.
        Console console = new Console(); // Crea una consola que observará la línea.
        line.addObserver(console); // Añade la consola como observadora de la línea.

        BufferedReader reader = new EditableBufferedReader(console, new InputStreamReader(System.in), line); // Crea el
                                                                                                             // lector
        // editable.

        try {
            String result = reader.readLine(); // Lee la línea editada por el usuario.
            System.out.println("\nLinea editada: " + result); // Muestra el resultado final después de que el usuario
            // presione Enter.
            System.out.println();
        } catch (IOException e) {
            e.printStackTrace(); // Muestra un error si ocurre algún problema durante la lectura.
        }
    }
}
