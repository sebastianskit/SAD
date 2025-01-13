import java.io.IOException;
import java.net.ServerSocket;

public class MyServerSocket {
    private ServerSocket serverSocket;

    public MyServerSocket(int port) throws IOException {
        this.serverSocket = new ServerSocket(port);
    }

    public MySocket accept() throws IOException {
        return new MySocket(serverSocket.accept());
    }

    public void close() {
        try {
            if (serverSocket != null)
                serverSocket.close();
        } catch (IOException e) {
            System.err.println("Error tancant el servidor: " + e.getMessage());
        }
    }
}
