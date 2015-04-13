package Lab3.Insect.State;

public class EatState implements State {
    @Override
    public void behavior() {
        System.out.print("Я ем! И становлюсь счастливее:)");
    }
}