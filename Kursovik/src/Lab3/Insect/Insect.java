package Lab3.Insect;
import Lab3.Insect.State.*;
/**
 * Created with IntelliJ IDEA.
 * User: Елизавета
 * Date: 12.11.12
 * Time: 12:22
 * To change this template use File | Settings | File Templates.
 */
public abstract class Insect {


    /**
     * name
     */
    private String name;
    /**
     * size (sm)
      */
    private int size;
    /**
     * age
     */
    private int age;
//---------------------------------------------
    private State state;
//---------------------------------------------

    /**
     * food
     */
    public enum Food{
        Растения, Животных, Навоз      //питаются растениями, животными, помётом(жук-навозник)
    }
    protected Food food;

    public Insect (String name, int size, int age, Food food){
        this.name=name;
        this.age=age;
        this.size=size;
        this.food=food;
    }

    public void View(){
           System.out.print("Привет! Меня зовут "+ name + ". "+ "Мне "+ age +" лет(года). ");
    }
    public void Eat() {
        System.out.print("Ням-ням!");
    }
    public void behavior(){
        state.behavior();
    }

    public void setState(State state) {
        this.state = state;
    }
}
