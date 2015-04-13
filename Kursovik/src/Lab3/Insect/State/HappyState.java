package Lab3.Insect.State;

public class HappyState implements State {
    @Override
    public void behavior() {
        System.out.println("Я счастливое насекомое!!");
    }
}