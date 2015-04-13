package Lab3.Insect;

import java.util.*;

/**
 * Так как насекомые живут стаями, то становится логичным создание коллекции - стая.
 * Для хранения коллеции была выбрана структура List, так как элементы коллекции могут повторяться
 */
public class InsectCollection<T extends Insect> {
    private ArrayList<Class<? extends T>> insectList = new ArrayList<Class<? extends T>>();
    public InsectCollection(){}
    public ArrayList<Class<? extends T>> getInsectList () {
          return insectList;
    }

}
