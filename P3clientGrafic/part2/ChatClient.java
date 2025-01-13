package part2;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.SocketChannel;

public class ChatClient {
    private SocketChannel clientChannel;
    private ChatClientGUI gui;

    public ChatClient(String host, int port) throws IOException {
        clientChannel = SocketChannel.open(new InetSocketAddress(host, port));
        gui = new ChatClientGUI(clientChannel);
        new Thread(this::listenForMessages).start();
    }

    private void listenForMessages() {
        ByteBuffer buffer = ByteBuffer.allocate(1024);
        while (true) {
            try {
                int bytesRead = clientChannel.read(buffer);
                if (bytesRead > 0) {
                    String message = new String(buffer.array(), 0, bytesRead);
                    gui.addMessage(message);
                    buffer.clear();
                }
            } catch (IOException e) {
                e.printStackTrace();
                break;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        new ChatClient("localhost", 12345);
    }
}