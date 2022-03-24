package DataStructure;

public class ArrayStack {
    static final int CAPACITY=1000;//设置栈的大小常数
    int top; //栈顶位置
    int stack[];//栈本身所在
    public ArrayStack(){
        this.top=-1;//表示空栈
        stack = new int[CAPACITY];
    }
    public boolean push(int val){
        if(top>=this.CAPACITY-1){
            //判断是否栈满
            System.out.println("Stack overflow!!!");
            return false;
        }
        stack[++top]=val;//先加1再赋值，因为初始值为—1
        return true;
    }
    public int pop(){
        /*
        * 删除并返回顶端元素*/
        if(top<0){
            System.out.println("Stack underflow!!!");
            return Integer.MIN_VALUE;
        }
        int val = this.stack[top--];//先赋值获得数据，在top-1
        return val;
    }
    public int peek(){
        /*观看顶端数据*/
        if(top<0){
            System.out.println("Stack underflow!!!");
            return Integer.MIN_VALUE;
        }
        int val = stack[top];
        return val;
    }

    public boolean isEmpty(){
        return top<0;
    }

    public static void main(String[] args){
        /*测试代码*/
        ArrayStack stack = new ArrayStack();
        int[] input = {2,3,0,1,4,5,6,7};
        for(int each: input){
            stack.push(each);
        }
        for(int i=0;i<input.length;i++){
            int num = stack.pop();
            System.out.println("the top number is: "+ num);
        }
    }
}
