import java.util.Observable;
import java.util.Observer;

@SuppressWarnings("deprecation")
public class Console implements Observer {

    @Override
    public void update(Observable o, Object arg) {
        if (o instanceof Line) {
            Line line = (Line) o;
            render(line);
        }
    }

    public void render(Line line) {
        clearConsole();
        System.out.print(line.getContent());
        moveCursorToPosition(line.getCursorPosition());
    }

    private void clearConsole() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

    private void moveCursorToPosition(int position) {
        System.out.print("\033[" + (position + 1) + "G");
    }
}
