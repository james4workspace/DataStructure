package DataStructure;

public class ArrayQueue {
    int front,rear,size;
    int CAPACITY = 10;//设定队列长度
    int array[];
    public ArrayQueue(){
        front = rear=this.size =0;
        array = new int[CAPACITY];
    }
    public void add(int val){
        if(this.isFUll()) return;
        array[rear]=val;
        rear=(rear+1)%CAPACITY;//找到新的位置
        size++;
        System.out.println(val+ " is enqueued.");
    }

    public int remove(){
        if(isEmpty()) return Integer.MIN_VALUE;
        int val = array[front];
        front = (front+1)%CAPACITY;
        size--;
        return val;
    }

    public int peek(){
        if(this.isEmpty()) return Integer.MIN_VALUE;
        return array[front];
    }

    public boolean isFUll(){
        return size ==this.CAPACITY;
    }
    public boolean isEmpty(){
        return size==0;
    }

    public static void main(String[] args){
        /*测试单元*/
        int[] input = {33,222,3,1,8,3,23,12,3,2232};
        ArrayQueue arrayQueue = new ArrayQueue();
        for(int each: input){
            arrayQueue.add(each);
        }
        for(int i=0;i<input.length;i++){
            System.out.println("remove the first item is: "+arrayQueue.remove());
        }
    }
}
