package DataStructure;

public class ArrayQueue2 {
    /*通过空一格，保证front的位置数据为0，头节点位置为front+1*/
    int front,rear;
    int CAPACITY = 10;//设定队列长度
    int array[];
    int realCapacity;

    public ArrayQueue2(){
        realCapacity=this.CAPACITY+1;
        front = rear=0;
        array=new int[realCapacity];
    }
    public void add(int val){
        if(this.isFUll()) return;
        rear = (rear+1)%realCapacity;//哪怕只有一个元素，也要保证rear = front +1
        array[rear]=val;//这里如果是一开始，那front依然为0，所以要想得到数据只能front+1
        System.out.println(val+ " is enqueued.");
    }

    public int remove(){
        if(isEmpty()) return Integer.MIN_VALUE;
        int val = array[front+1];
        front = (front+1)%realCapacity;
        return val;
    }

    public int peek(){
        if(this.isEmpty()) return Integer.MIN_VALUE;
        return array[front+1];
    }

    public boolean isFUll(){
        return front == (rear+1)%realCapacity;//如果front就在rear之后一位，那就表示到头了
    }
    public boolean isEmpty(){
        return front == rear;
    }

    public static void main(String[] args){
        /*测试单元*/
        int[] input = {33,222,3,1,8,3,23,12,3,2232};
        ArrayQueue2 arrayQueue = new ArrayQueue2();
        for(int each: input){
            arrayQueue.add(each);
        }
        for(int i=0;i<input.length;i++){
            System.out.println("remove the first item is: "+arrayQueue.remove());
        }
    }
}
