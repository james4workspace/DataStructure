package DataStructure;

import java.util.*;
public class IteratorStudy {
    public static void main(String[] args){
        ArrayList list = new ArrayList();
        list.add("a");
        list.add("b");
        list.add("c");
        Iterator it = list.iterator();
        while(it.hasNext()){
            String str = (String) it.next();
            System.out.println(str);
        }
    }
}
