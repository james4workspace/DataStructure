package DataStructure;

import java.util.Scanner;
import java.util.*;
public class MaxHeap {
    private int CAPACITY;//常数，表示heap的大小
    private int size =0;
    private int[] array;

    public MaxHeap(int capacity){
        this.CAPACITY = capacity;
        array = new int[this.CAPACITY];
    }
    private int getLeftChildIndex(int parentIndex){
        /*获得左子树节点*/
        return 2*parentIndex+1;//0节点左子节点是1，右子节点是2,1左子节点是3，右子节点是4；
    }
    private int getRightChildIndex(int parentIndex){
        /*获得右子树节点*/
        return 2*parentIndex+2;//0节点左子节点是1，右子节点是2,1左子节点是3，右子节点是4；
    }
    private int getParentIndex(int childIndex){
        /*获得父子树节点*/
        return(childIndex-1)/2;//因为是integer，所以1/2会直接为0，3/2会直接为1；
    }

    private boolean hasLeftChild(int index){
        return getLeftChildIndex(index)<size;
    }
    private boolean hasRightChild(int index){
        return getRightChildIndex(index)<size;
    }
    private boolean hasParent(int index){
        return getParentIndex(index)>=0;
    }
    private int leftChild(int parentIndex){
        return array[getLeftChildIndex(parentIndex)];
    }
    private int rightChild(int parentIndex){
        return array[getRightChildIndex(parentIndex)];
    }
    private int parent(int child){
        return array[getParentIndex(child)];
    }

    public void insert(int item){
        if(size==CAPACITY){
            array=Arrays.copyOf(array,CAPACITY*2);
        }
        array[size]=item;
        size++;
        heapifyUp();//往上对比替换
    }
    private void heapifyUp(){
        int index = size-1;
        while(hasParent(index)&&parent(index)<array[index]){
            swap(getParentIndex(index),index);
            index = getParentIndex(index);
        }
    }

    private void swap(int parentIndex,int childIndex){
        int temp = array[parentIndex];
        array[parentIndex] = array[childIndex];
        array[childIndex] = temp;
    }

    private int poll(){
        if(size==0){
            System.out.println("the heap is empty!!!");
            return Integer.MIN_VALUE;
        }
        int element = array[0];
        array[0]=array[size-1];
        size--;
        heapifyDown();
        return element;
    }

    private void heapifyDown(){
        int index=0;
        while(hasLeftChild(index)){
            int largerChildIndex = getLeftChildIndex(index);
            if(hasRightChild(index)&&rightChild(index)>leftChild(index)){
                largerChildIndex = getRightChildIndex(index);
            }
            if(array[index]<array[largerChildIndex]){
                swap(index,largerChildIndex);
            }else{
                break;
            }
            index = largerChildIndex;
        }
    }

    private int peek(){
        if(size==0){
            throw new NoSuchElementException();//没有就抛出异常
        }
        return array[0];
    }

    public static void main(String[] args){
        /*测试代码ACM模式*/
        Scanner obj = new Scanner(System.in);
        System.out.println("Please enter the list of numbers for input, " +
                "and the last number is how many points you want to pop.\n " +
                "As ending, you need to input any characters that are not numbers.");
        List<Integer> input = new ArrayList<>();
        while(obj.hasNextInt()){
            input.add(obj.nextInt());
        }
        int poppedNum = input.remove(input.size()-1);
        MaxHeap mHeap = new MaxHeap(5);
        for(int i=0;i<input.size();i++){
            mHeap.insert(input.get(i));
        }
        for(int i=0;i<poppedNum;i++){
            System.out.println("the popped number is: "+ mHeap.poll());
        }
    }
}
