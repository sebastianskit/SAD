package part1;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.nio.ByteBuffer;
import java.nio.channels.*;
import java.util.Iterator;

public abstract class GenericServer {
    private Selector selector;
    private ServerSocketChannel serverChannel;

    public GenericServer(int port) throws IOException {
        selector = Selector.open();
        serverChannel = ServerSocketChannel.open();
        serverChannel.bind(new InetSocketAddress(port));
        serverChannel.configureBlocking(false);
        serverChannel.register(selector, SelectionKey.OP_ACCEPT);
    }

    public void start() throws IOException {
        while (true) {
            selector.select();
            Iterator<SelectionKey> keys = selector.selectedKeys().iterator();
            while (keys.hasNext()) {
                SelectionKey key = keys.next();
                keys.remove();
                if (!key.isValid())
                    continue;
                if (key.isAcceptable())
                    accept(key);
                if (key.isReadable())
                    read(key);
            }
        }
    }

    protected void accept(SelectionKey key) throws IOException {
        ServerSocketChannel serverChannel = (ServerSocketChannel) key.channel();
        SocketChannel clientChannel = serverChannel.accept();
        clientChannel.configureBlocking(false);
        clientChannel.register(selector, SelectionKey.OP_READ);
    }

    private void read(SelectionKey key) throws IOException {
        SocketChannel clientChannel = (SocketChannel) key.channel();
        ByteBuffer buffer = ByteBuffer.allocate(1024);
        int bytesRead = clientChannel.read(buffer);
        if (bytesRead == -1) {
            clientChannel.close();
            key.cancel();
            return;
        }
        handleData(clientChannel, buffer.array(), bytesRead);
    }

    protected abstract void handleData(SocketChannel clientChannel, byte[] data, int bytesRead) throws IOException;
}
