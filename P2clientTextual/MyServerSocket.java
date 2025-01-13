import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class MyServerSocket {
    public ServerSocket ss;

    public MyServerSocket(int port) {
        try {
            ss = new ServerSocket(port);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public MySocket accept() {

        try {
            Socket s = ss.accept();
            return new MySocket(s);
        } catch (IOException e) {
            System.out.println(e);
            return null;
        }
    }
}
