package Lab3.Insect.ChildInsect;

import Lab3.Insect.Insect;

public class LadyBug extends Bug {
    public LadyBug(String name, int size, int age, Food food) {
        super(name, size, age, food);
    }
    public int [][][] population = new int[][][] {{{1,2,3},{12,23,22}},{{4,5,6}}};
    public void population(int countOfLadyBugs, int realCount) {
          if(countOfLadyBugs == 1 )
          {
              realCount=population[1][2][0];
              System.out.println(realCount);
          }

    }
}