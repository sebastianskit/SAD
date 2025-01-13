import java.io.*;
import java.net.Socket;

public class MySocket {
    private Socket socket;
    private BufferedReader in;
    private PrintWriter out;

    public MySocket(Socket socket) {
        this.socket = socket;
        initializeStreams();
    }

    public MySocket(String host, int port) throws IOException {
        this.socket = new Socket(host, port);
        initializeStreams();
    }

    private void initializeStreams() {
        try {
            in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            out = new PrintWriter(socket.getOutputStream(), true);
        } catch (IOException e) {
            System.err.println("Error inicialitzant streams: " + e.getMessage());
        }
    }

    public void println(String message) {
        out.println(message);
    }

    public String readLine() throws IOException {
        return in.readLine();
    }

    public void close() {
        try {
            if (in != null)
                in.close();
            if (out != null)
                out.close();
            if (socket != null)
                socket.close();
        } catch (IOException e) {
            System.err.println("Error tancant el socket: " + e.getMessage());
        }
    }
}
