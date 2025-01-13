package P2clientextual;

import java.io.IOException;
import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

public class Server {

    private static final int PORT = 8080;
    private static Map<String, MySocket> clientDictionary = new ConcurrentHashMap<>();

    public static void main(String[] args) throws IOException {

        MyServerSocket myServerSocket = new MyServerSocket(PORT);
        System.out.println("Server STARTED!!!");

        while (true) {
            MySocket client = myServerSocket.accept();
            client.printLine("Conectado!!");

            new Thread(() -> {
                client.printLine("Introduce tu nombre de usurario, UserName: ");
                String name = client.readLine();
                client.printLine("Hola " + name + ", estas en el nuevochat!");
                clientDictionary.put(name, client);
                String text;
                while ((text = client.readLine()) != null) {
                    broadcast(text, name);
                    System.out.println(name + " says: " + text);
                }
                System.out.println(name + " has left the chat");
                clientDictionary.remove(name);
                client.close();
            }).start();
        }
    }

    public static void broadcast(String message, String name) {
        for (Map.Entry<String, MySocket> entry : clientDictionary.entrySet()) {
            String actualUser = entry.getKey();
            MySocket actualSocket = entry.getValue();
            if (!actualUser.equals(name)) {
                actualSocket.printLine(name + "> " + message);
            }
        }
    }
}
