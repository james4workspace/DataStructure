package DataStructure;

public class LinkedStack {
    static class StackNode{
        int val;
        StackNode next;
        StackNode(int val){
            this.val=val;
        }
    }

    StackNode top;
    public LinkedStack(){
        top =null;
    }

    public void push(int val){
        StackNode newNode = new StackNode(val);
        if(top==null){
            top = newNode;
        }else{
            StackNode temp = top;
            top = newNode;
            top.next = temp;
        }
    }

    public int pop(){
        if(top==null){
            System.out.println("Stack is empty!!");
            return Integer.MIN_VALUE;
        }
        int popped = top.val;
        top = top.next;
        return popped;
    }

    public int peek(){
        if(top==null){
            System.out.println("Stack is empty!!");
            return Integer.MIN_VALUE;
        }
        return top.val;
    }
    public boolean isEmpty(){
        return top == null;
    }

    public static void main(String[] args){
        /*单元测试代码*/
        LinkedStack stack = new LinkedStack();
        int[] nums =new int[]{3,2,1,4,5,6,7,8,9,100,2321,233};
        for(int each:nums){
            stack.push(each);
        }
        for(int i=0;i<nums.length;i++){
            int num = stack.pop();
            System.out.println("the top number is: "+num);
        }
        System.out.println("the stack is empty: "+ stack.isEmpty());
    }
}
