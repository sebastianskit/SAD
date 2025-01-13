import java.io.IOException;
import java.util.concurrent.ConcurrentHashMap;
import java.util.Map;

public class ChatServer {
    private static final int PORT = 12345;
    private Map<String, MySocket> clients = new ConcurrentHashMap<>();

    public static void main(String[] args) {
        new ChatServer().start();
    }

    public void start() {
        try (MyServerSocket serverSocket = new MyServerSocket(PORT)) {
            System.out.println("Servidor en funcionament al port " + PORT);

            while (true) {
                MySocket clientSocket = serverSocket.accept();
                new Thread(() -> handleClient(clientSocket)).start();
            }
        } catch (IOException e) {
            System.err.println("Error del servidor: " + e.getMessage());
        }
    }

    private void handleClient(MySocket clientSocket) {
        try {
            clientSocket.println("Benvingut! Introdueix el teu nick:");
            String nick = clientSocket.readLine();

            if (nick == null || nick.trim().isEmpty() || clients.containsKey(nick)) {
                clientSocket.println("Nick no vàlid o ja utilitzat. Desconnectant.");
                clientSocket.close();
                return;
            }

            clients.put(nick, clientSocket);
            System.out.println(nick + " s'ha connectat.");
            broadcast("** " + nick + " s'ha unit al xat. **", null
