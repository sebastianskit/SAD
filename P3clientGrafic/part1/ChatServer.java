package part1;

import java.io.IOException;
import java.nio.channels.SocketChannel;
import java.nio.ByteBuffer;
import java.nio.channels.SelectionKey;
import java.util.HashSet;
import java.util.Set;

public class ChatServer extends GenericServer {
    private Set<SocketChannel> clients = new HashSet<>();

    public ChatServer(int port) throws IOException {
        super(port);
    }

    @Override
    protected void handleData(SocketChannel clientChannel, byte[] data, int bytesRead) throws IOException {
        String message = new String(data, 0, bytesRead);
        broadcastMessage(clientChannel, message);
    }

    private void broadcastMessage(SocketChannel sender, String message) throws IOException {
        for (SocketChannel client : clients) {
            if (client != sender) {
                client.write(ByteBuffer.wrap(message.getBytes()));
            }
        }
    }

    @Override
    protected void accept(SelectionKey key) throws IOException {
        super.accept(key);
        clients.add((SocketChannel) key.channel());
    }
}
