package P2clientTextual;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;

public class MySocket extends Socket {

    public Socket sck;

    public BufferedReader reader;

    public PrintWriter wr;

    public String nick;

    int port;

    public MySocket(Socket socket) throws IOException {
        try {
            this.sck = socket;
            this.reader = new BufferedReader(new InputStreamReader(sck.getInputStream()));
            this.wr = new PrintWriter(new OutputStreamWriter(sck.getOutputStream()));
        } catch (IOException ex) {
            throw new IOException("Error al inicializar MySocket", ex);
        }

    }

    public MySocket(String host, int port) throws IOException {
        try {
            this.port = port;
            sck = new Socket(host, port);
            this.reader = new BufferedReader(new InputStreamReader(sck.getInputStream()));
            this.wr = new PrintWriter(new OutputStreamWriter(sck.getOutputStream()));
        } catch (IOException ex) {
            throw new IOException("Error al inicializar MySocket", ex);
        }
    }

    public Socket getSocket() {
        return this.sck;
    }

    //
    public String getNick() {
        return nick;
    }

    public void setNick(String nick) {
        this.nick = nick;
    }

    public int getPort() {
        return this.port;
    }

    public String readLine() {
        String line = null;
        try {
            line = reader.readLine();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
        return line;
    }

    public int readInt() {
        return Integer.parseInt(readLine());
    }

    public Double readDOuble() {
        return Double.parseDouble(readLine());
    }

    public Boolean readBool() {
        return Boolean.parseBoolean(readLine());
    }

    public Short readSHort() {
        return Short.parseShort(readLine());
    }

    public Long readLong() {
        return Long.parseLong(readLine());
    }

    public Byte readByte() {
        return Byte.parseByte(readLine());
    }

    public void printLine(String line) {

        wr.println(line);

    }

    public void printInt(int num) {
        wr.println(num);

    }

    public void printDouble(Double dob) {
        wr.println(dob);

    }

    public void printBool(Boolean bool) {
        wr.println(bool);

    }

    public void printByte(Byte byt) {
        wr.println(byt);

    }

    public void close() {
        try {
            wr.close();
            reader.close();
            sck.close();
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
}