package Lab3.Insect.ChildInsect;
import Lab3.Insect.*;

public class Butterfly extends Insect implements Flyable {
    public Butterfly(String name, int size, int age, Food food) {
        super(name, size, age, food);
    }
    public void View(Insect i) {
        super.View();
        System.out.println("Я бабочка!");
    }
    public void Eat() {
        super.Eat();
        System.out.println(" Я кушаю нектар, как и все бабочки!");
    }
    public void fly() {
        //To change body of implemented methods use File | Settings | File Templates.
    }
}