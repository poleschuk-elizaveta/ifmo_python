package Lab3.Insect.ChildInsect;
import Lab3.Insect.*;

public class Bug extends Insect {
    public Bug(String name, int size, int age, Food food) {
        super(name, size, age, food);
    }
    public void View(Insect i) {
        super.View();
        System.out.println("Я жук!");
    }
    public void Eat() {
        super.Eat();
        System.out.println("Я кушаю "+food.toString()+ ", как и все жуки.");
    }
    public void Eat(String s) {
        System.out.println("Я кушаю "+food.toString()+ ", как и все жуки." + s);
    }
}