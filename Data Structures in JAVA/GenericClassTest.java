package DataStructure;

public class GenericClassTest {
    public static class Box<E>{
        private E t;
        public void add(E t){
            this.t = t;
        }
        public E get(){
            return t;
        }
    }
    public static void main(String[] args){
        Box<Integer> intBox=new Box<>();
        Box<String> strBox = new Box<>();

        intBox.add(10);
        strBox.add("Hello World");

        System.out.printf("整数型数值为： %d\n",intBox.get());
        System.out.printf("字符串为： %s\n",strBox.get());
    }
}
