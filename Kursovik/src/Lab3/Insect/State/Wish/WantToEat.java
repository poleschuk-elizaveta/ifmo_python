package Lab3.Insect.State.Wish;
import Lab3.Insect.State.*;

public class WantToEat implements State {
    @Override
    public void behavior() {
        System.out.print("Я хочу есть!");
    }
}