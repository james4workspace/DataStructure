package DataStructure;

import java.util.*;
public class LinkedList {
    static class ListNode{
        int val;
        ListNode next;
        public ListNode(int val){
            this.val = val;
        }
    }
    ListNode head;//头指针
    ListNode tail;//尾指针
    int size; //链长
    public LinkedList(){
        /*
        * 构建器
         */
        head = null;//相当于python的None
        tail = null;
        size = 0;
    }
    public boolean insert(int position,int number){
        /*
        * 插入到链表内*/
        if(position>size){
            return false;
        }
        ListNode newNode = new ListNode(number);//该位置数据
        if(position ==0){
            //插入为头结点
            newNode.next = head;
            head = newNode;
            if(tail==null){
                tail = newNode;
            }
        }
        else if(position==size){
            //插入为尾节点
            this.append(number);//直接通过调用类内函数append
            //this 类似于python的self，起到自引用的作用
        }
        else{
            ListNode prev = head;
            for(int i=0;i<position-1;i++){
                prev = prev.next;
            }
            ListNode next = prev.next;
            newNode.next = next;
            prev.next = newNode;
        }
        size++;
        return true;
    }

    public void append(int number){
        /*
        * 添加到末尾的函数*/
        ListNode newNode = new ListNode(number);
        if(tail==null){//即空列表
            this.head = newNode;
            this.tail = newNode;
            this.size ++;
        }
        else{
            this.tail.next = newNode;
            this.tail = newNode;
            this.size++;
        }
    }
    public boolean delete(int number){
        /*
        * 删除函数*/
        if(head!=null&&head.val==number){
            //删除头结点
            this.head = head.next;
            size--;
            if(size==0){
                tail=head;
            }
            return true;
        }
        else{
            ListNode prev = head;
            ListNode cur = head;
            while(prev!=null && cur!=null){
                if(cur.val==number){
                    if(cur==tail){//删除尾节点
                        tail=prev;
                    }
                    prev.next = cur.next;
                    size--;
                    return true;
                }
                prev = cur;
                cur = cur.next;
            }
        }
        return false;
    }

    public int search(int number){
        /*
        * 查找该数据的位置*/
        ListNode cur = head;
        int index = 0;
        while(cur!=null){
            if(cur.val==number){
                return index;
            }
            cur=cur.next;
            index++;
        }
        return -1;//如果找不到则return -1
    }

    public List<Integer> showAll(){
        List<Integer> allList = new ArrayList<>();
        ListNode cur = this.head;
        while(cur!=null){
            allList.add(cur.val);
            cur =cur.next;
        }
        return allList;
    }

    public static void main(String[] args){
        /*
        * 单元测试代码*/
        LinkedList linkedList = new LinkedList();
        int[] input = new int[]{2,3,1,2,5,6};
        for (int each: input){
            linkedList.append(each);
        }
        List<Integer> output = linkedList.showAll();
        System.out.println(output.toString());
        linkedList.delete(3);
        output = linkedList.showAll();
        System.out.println(output.toString());
        System.out.println(linkedList.search(5));
        linkedList.insert(3,6);
        output = linkedList.showAll();
        System.out.println(output.toString());
    }
}
