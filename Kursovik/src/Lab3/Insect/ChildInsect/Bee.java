package Lab3.Insect.ChildInsect;
import Lab3.Insect.*;

public class Bee extends Insect implements Flyable {
    public Bee(String name, int size, int age, Insect.Food food) {
        super(name, size, age, food);
    }

    @Override
    public void View() {
        super.View();
        System.out.println("Я пчёлка!");
    }

    /**
     * Пчела летает
      */
    public void fly() {
        System.out.println("Берегись! Летит пчела! Бж-ж-ж-ж!");
    }

    /**
     * Пчела ест
     */
    public void Eat() {
        super.Eat();
        System.out.println(" Я кушаю пыльцу, как и все пчёлки!");
    }
}