public class Line {
    private StringBuilder content;
    private int cursorPosition;

    public Line() {
        content = new StringBuilder();
        cursorPosition = 0;
    }

    public void insertChar(char c) {
        content.insert(cursorPosition, c);
        cursorPosition++;
    }

    public void deleteChar() {
        if (cursorPosition > 0) {
            content.deleteCharAt(cursorPosition - 1);
            cursorPosition--;
        }
    }

    public void moveCursorLeft() {
        if (cursorPosition > 0) {
            cursorPosition--;
        }
    }

    public void moveCursorRight() {
        if (cursorPosition < content.length()) {
            cursorPosition++;
        }
    }

    public String getContent() {
        return content.toString();
    }

    public int getCursorPosition() {
        return cursorPosition;
    }

    // Altres mètodes necessaris per a l'edició
}

