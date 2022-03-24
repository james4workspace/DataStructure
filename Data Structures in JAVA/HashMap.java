package DataStructure;


import java.util.*;
import java.util.Scanner;
public class HashMap {
    static class HashNode{
        /*哈希表节点*/
        String key;
        Integer value;
        HashNode next;
        public HashNode(String key, Integer value){
            this.key = key;
            this.value = value;
            this.next = null;
        }
    }
    private List<HashNode> bucketArray;
    private int numBuckets;//bucketArray长度
    private int size;//多少个元素
    public HashMap(){
        bucketArray =new ArrayList<>();
        numBuckets = 10;//简单定义为10 的案例
        size =0;
        for(int i=0;i<numBuckets;i++){
            bucketArray.add(null);//initialization -> bucketArray;
        }
    }
    private int getBucketIndex(String key){
        /*这里是哈希函数，把key值转换为哈希值*/
        int hashCode = key.hashCode();
        //JAVA虚拟机本身会自动给string直接生成hash code，不需要我们自己写
        int index = hashCode % numBuckets;//这里通过除MOD取余法计算index值
        return index;
    }
    public void add(String key, Integer value){
        int bucketIndex = getBucketIndex(key);
        HashNode head= bucketArray.get(bucketIndex);//获得位置index的元素
        //head是链地址法里链的头结点
        while(head!=null){
            if(head.key.equals(key)){
                //如果key值相同，意味着修改
                head.value = value;
                return;
            }
            head = head.next;
        }//循环结束也没有找到key，说明不存在该key的数据，进行添加
        head = bucketArray.get(bucketIndex);
        HashNode newNode = new HashNode(key,value);
        newNode.next = head;
        bucketArray.set(bucketIndex,newNode);
        size++;
        if((1.0*size)/numBuckets>=0.7){
            //保证存储的数据不要太多，导致冲突过多
            generateBiggerArray();
        }
    }

    private void generateBiggerArray(){
        /*扩容，将现有的bucketArray移到新的bucketArray上*/
        List<HashNode> temp = bucketArray;
        bucketArray = new ArrayList<>();
        numBuckets = 2 * numBuckets;
        for(int i=0;i<numBuckets;i++) {
            bucketArray.add(null);
        }
        for(HashNode headNode:temp){
            while(headNode!=null){
                add(headNode.key,headNode.value);
                headNode = headNode.next;
            }
        }
    }
    public Integer get(String key){
        /*查询函数*/
        int bucketIndex = getBucketIndex(key);
        HashNode head = bucketArray.get(bucketIndex);
        while(head!=null){
            if(head.key.equals(key)){
                return head.value;
            }
            head=head.next;
        }
        return null;
    }

    public Integer remove(String key){
        /*链表中删除节点的函数*/
        int bucketIndex = getBucketIndex(key);
        HashNode head = bucketArray.get(bucketIndex);
        HashNode prev = null;
        while(head!=null){
            if(head.key.equals(key)){
                break;
            }
            prev = head;
            head = head.next;
        }
        if(head == null){
            //没找到
            return null;
        }
        if(prev == null){
            //删除头结点
            bucketArray.set(bucketIndex, head.next);
        }
        else{
            prev.next = head.next;
        }
        size--;
        return head.value;
    }

    public boolean isEmpty() {
        return size==0;
}
    public static void main(String[] args){
        /*测试代码*/
        Scanner obj = new Scanner(System.in);
        System.out.println("Please enter the hash table node with format: key value \\n");
        HashMap hashMap=new HashMap();
        List<String> keyList = new ArrayList<>();
        while(obj.hasNextLine()){
            String strIn=obj.nextLine();
            String[] strList = strIn.split(" ");
            String key = strList[0];
            Integer value = Integer.parseInt(strList[1]);
            hashMap.add(key,value);
            keyList.add(key);
        }
        for(String each: keyList){
            System.out.println("the pair is: "+each+": "+hashMap.get(each));
        }
    }
}
