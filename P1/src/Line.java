import java.util.Observable;

@SuppressWarnings("deprecation")
public class Line extends Observable {
    private StringBuilder content;
    private int cursorPosition;

    public Line() {
        this.content = new StringBuilder();
        this.cursorPosition = 0;
    }

    public String getContent() {
        return content.toString();
    }

    public int getCursorPosition() {
        return cursorPosition;
    }

    public void insertChar(char ch) {
        content.insert(cursorPosition, ch);
        cursorPosition++;
        setChanged();
        notifyObservers();
    }

    public void deleteChar() {
        if (cursorPosition > 0) {
            content.deleteCharAt(cursorPosition - 1);
            cursorPosition--;
            setChanged();
            notifyObservers();
        }
    }

    public void moveCursorLeft() {
        if (cursorPosition > 0) {
            cursorPosition--;
            setChanged();
            notifyObservers();
        }
    }

    public void moveCursorRight() {
        if (cursorPosition < content.length()) {
            cursorPosition++;
            setChanged();
            notifyObservers();
        }
    }

    public void moveCursorHome() {
        cursorPosition = 0;
        setChanged();
        notifyObservers();
    }

    public void moveCursorEnd() {
        cursorPosition = content.length();
        setChanged();
        notifyObservers();
    }

    public void reset() {
        content.setLength(0);
        cursorPosition = 0;
        setChanged();
        notifyObservers();
    }
}
