package Lab3.Insect;

import Lab3.Insect.ChildInsect.*;
import Lab3.Insect.State.EatState;
import Lab3.Insect.State.HappyState;

/**
 * Created with IntelliJ IDEA.
 * User: Елизавета
 * Date: 27.11.12
 * Time: 0:03
 * To change this template use File | Settings | File Templates.
 */
public class TestInsect {
    //Insect.Food food= Insect.Food.Навоз;



    static public void main(String[] arg)
    {
        Bug bug=new Bug("Дуся", 50, 2, Insect.Food.Навоз);
        bug.View(bug);
        bug.Eat();
        bug.Eat(" C аппетитом!");
        System.out.println("  ");
        Bee bee=new Bee("Майя", 50, 3, Insect.Food.Растения);
        bee.View();
        bee.fly();
      //  bee.behavior();
        bee.Eat();
        bee.setState(new HappyState());
        bee.behavior();
    }
}