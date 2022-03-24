package DataStructure;

public class LinkedQueue {
    static class QueueNode{
        int val;
        QueueNode next;
        QueueNode(int val){
            this.val=val;
            this.next = null;
        }
    }
    QueueNode front;
    QueueNode rear;

    public void add(int val){
        QueueNode newNode = new QueueNode(val);
        if(this.rear==null){
            //queue is empty
            this.front=this.rear=newNode;
            return;
        }
        rear.next=newNode;
        rear = newNode;
    }

    public int remove(){
        if(this.front==null){
            System.out.println("The Queue is empty!!!");
            return Integer.MIN_VALUE;
        }
        QueueNode frontNode=this.front;
        this.front = front.next;
        if(front==null){
            rear=null;
        }
        return frontNode.val;
    }

    public boolean isEmpty(){
        return front==null;
    }
    public static void main(String[] args){
        /*测试单元*/
        int[] input = {33,222,3,1,8,3,23,12,3,2232};
        LinkedQueue arrayQueue = new LinkedQueue();
        for(int each: input){
            arrayQueue.add(each);
        }
        for(int i=0;i<input.length;i++){
            System.out.println("remove the first item is: "+arrayQueue.remove());
        }
    }
}
