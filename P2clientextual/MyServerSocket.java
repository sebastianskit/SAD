
package P2clientextual;

import java.net.ServerSocket;
import java.io.IOException;

public class MyServerSocket extends ServerSocket {

    private ServerSocket serverSocket;
    private boolean connected;

    // Constructor que crea un socket de servidor vinculado al puerto especificado
    public MyServerSocket(int port) throws IOException {
        this.serverSocket = new ServerSocket(port);
        this.connected = true;
    }

    public int getLocalPort() {
        return serverSocket.getLocalPort();
    }

    public boolean isBound() {
        return connected;
    }

    public boolean isClosed() {
        return !connected;
    }

    // Con esta funcion escuchamos y aceptamos conexiones entrantes
    public MySocket accept() {
        try {
            if (connected) {
                return new MySocket(serverSocket.accept());
            } else {
                return null;
            }
        } catch (IOException ex) {
            ex.printStackTrace();
            return null;
        }
    }

    // Cierra el socket
    public void close() {
        try {
            connected = false;
            if (this.serverSocket != null && !this.serverSocket.isClosed()) {
                serverSocket.close();
            }
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}