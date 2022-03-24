package DataStructure;

import java.util.Scanner;
public class PriorityQueue {
    static class Node{
        int val;
        int priority;
        Node next;
        public Node(int val, int priority){
            this.val=val;
            this.priority=priority;
            this.next = null;
        }
    }

    Node head = null;

    public void push(int val,int priority){
        if(head==null){
            head = new Node(val,priority);
            return;
        }
        Node cur = head;
        Node newNode = new Node(val,priority);
        if(head.priority<priority){
            //如果头节点非最优
            newNode.next = head;
            this.head = newNode;
        }
        else{
            //根据优先级插入到链中
            while(cur.next!=null&&cur.next.priority>priority){
                // && 表示如果前一个目标不成立，不会判断后一个目标，所以即便前一个为null，后一个不受影响
                cur = cur.next;
            }
            newNode.next=cur.next;
            cur.next = newNode;
        }
    }

    public Node peek(){
        return head;
    }

    public Node pop(){
        if(head==null){
            System.out.printf("empty queue!!!");
            return null;
        }
        Node temp = head;
        head = head.next;
        return temp;
    }

    public boolean isEmpty(){
        return head == null;
    }

    public static void main(String[] args){
        Scanner obj = new Scanner(System.in);
        System.out.println("Please Enter the list of numbers, making the first line " +
                "as value list, the second line as priority list");
        while(obj.hasNext()){

            String str1 = obj.nextLine();
            String str2 = obj.nextLine();
            String[] str1_list = str1.split(" ");
            String[] str2_list = str2.split(" ");
            int[] values = new int[str1_list.length];
            int[] priorities = new int[str2_list.length];
            PriorityQueue que = new PriorityQueue();
            System.out.println(que.isEmpty());
            for(int i=0;i<str1_list.length;i++){
                values[i]=Integer.parseInt(str1_list[i]);
                priorities[i] = Integer.parseInt(str2_list[i]);
                que.push(values[i],priorities[i]);
            }
            for(int i=0;i<3;i++){
                Node popped = que.pop();
                System.out.println("the popped number is: "+popped.val);
                System.out.println("the popped priority is: "+popped.priority);
            }
        }
    }
}
