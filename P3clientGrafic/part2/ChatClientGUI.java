package part2;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.SocketChannel;

public class ChatClientGUI extends JFrame {
    private JTextArea messageArea;
    private JTextField inputField;
    private JList<String> userList;
    private DefaultListModel<String> userModel;
    private SocketChannel clientChannel;

    public ChatClientGUI(SocketChannel clientChannel) {
        this.clientChannel = clientChannel;
        setTitle("Chat Client");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        messageArea = new JTextArea();
        messageArea.setEditable(false);
        add(new JScrollPane(messageArea), BorderLayout.CENTER);

        inputField = new JTextField();
        inputField.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                sendMessage();
            }
        });
        add(inputField, BorderLayout.SOUTH);

        userModel = new DefaultListModel<>();
        userList = new JList<>(userModel);
        add(new JScrollPane(userList), BorderLayout.EAST);

        setVisible(true);
    }

    private void sendMessage() {
        String message = inputField.getText();
        try {
            clientChannel.write(ByteBuffer.wrap(message.getBytes()));
            inputField.setText("");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void addMessage(String message) {
        messageArea.append(message + "\n");
    }

    public void addUser(String user) {
        userModel.addElement(user);
    }

    public void removeUser(String user) {
        userModel.removeElement(user);
    }
}