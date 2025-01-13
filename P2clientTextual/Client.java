
package P2clientTextual;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Client {

    public static void main(String[] args) throws IOException {

        MySocket sc = new MySocket(args[0], Integer.parseInt(args[1]));

        BufferedReader BuffR = new BufferedReader(new InputStreamReader(System.in));

        // Input threat (keyboard)
        new Thread(() -> {
            String line;
            try {
                while ((line = BuffR.readLine()) != null) {
                    sc.printLine(line);
                    if (line.matches("exit")) {
                        sc.close();
                        break;
                    }
                }
                sc.printLine("exit");
                sc.close();
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }).start();

        new Thread(() -> {
            String line;
            while ((line = sc.readLine()) != null) {
                if (line.matches("exit")) {
                    break;
                }
                System.out.println(line);
            }
            System.out.println("Client Disconnected!!!");
            sc.close();
            System.exit(0);
        }).start();
    }
}