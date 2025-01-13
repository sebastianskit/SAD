import java.io.IOException;
import java.util.Scanner;

public class Client {
    private static final String SERVER_HOST = "localhost";
    private static final int SERVER_PORT = 12345;

    public static void main(String[] args) {
        try (MySocket clientSocket = new MySocket(SERVER_HOST, SERVER_PORT)) {
            Scanner scanner = new Scanner(System.in);
            System.out.println(clientSocket.readLine()); // Missatge de benvinguda

            // Thread per llegir missatges del servidor
            new Thread(() -> {
                String message;
                try {
                    while ((message = clientSocket.readLine()) != null) {
                        System.out.println(message);
                    }
                } catch (IOException e) {
                    System.err.println("Error al rebre dades del servidor: " + e.getMessage());
                }
            }).start();

            // Thread per enviar missatges al servidor
            String userInput;
            while ((userInput = scanner.nextLine()) != null) {
                clientSocket.println(userInput);
            }
        } catch (IOException e) {
            System.err.println("Error connectant al servidor: " + e.getMessage());
        }
    }
}
