package DataStructure;

import java.util.Scanner;
import java.util.*;
import java.util.PriorityQueue;
import java.util.ArrayList;
public class GreedyAlgorithm {
    int[] choices;
    private GreedyAlgorithm(int[] choices){
        this.choices = choices;
    }

    static class ReturnNode{
        /* 这里定义了一个新的类，方便返回一个包含置换硬币数量以及置换硬币的列表的广义表
        *  题目并不要求形成广义表，这里是为了进一步理解贪心算法
        * */
        int changeNum;
        List<Integer> changeList;
        private ReturnNode(int changeNum,ArrayList<Integer> changeList){
            this.changeNum=changeNum;
            this.changeList = changeList;
        }
    }

    private ReturnNode getSmallestNum(int num){
        /* 这里我们使用贪心算法Greedy Algorithm，追求局部最优解
        *  这里的局部最优解在哪儿呢？在于每一步都选择最大的coin，直到最后超出的时候，再返回选择次大的coin，以此类推，直到抵达最终值
        * */
        if(num==0){
            return null;
        }
        //建立一个优先队列，遵循最大Heap原理
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
        for(int each:this.choices){
            maxHeap.add(each);
        }
        ArrayList<Integer> changeList = new ArrayList<>();
        ReturnNode ans = new ReturnNode(0,changeList);
        int sumSofar=0;
        ans = countSum(ans,sumSofar,num,maxHeap);
        return ans;
    }

    private ReturnNode countSum(ReturnNode ans,int sumSofar, int num,PriorityQueue<Integer> maxHeap){
        int maxCoin = maxHeap.poll();
        while(sumSofar<num){
            //这里只要合小于最终值，不断循环添加最大的coin
            ans.changeList.add(maxCoin);
            sumSofar+=maxCoin;
        }
        if(sumSofar==num){
            //如果达到最终值，则返回
            ans.changeNum=ans.changeList.size();
            return ans;
        }
        ans.changeList.remove(ans.changeList.size()-1);//删除最后一位，再重新回去计算
        sumSofar-=maxCoin;
        ans = countSum(ans,sumSofar,num,maxHeap);
        return ans;
    }

    public static void main(String[] args){
        Scanner obj = new Scanner(System.in);
        int[] coinChoices =new int[]{5,2,1};//这里是硬币的选项
        GreedyAlgorithm ga = new GreedyAlgorithm(coinChoices);
        System.out.printf("Please enter the sum you want to change for the coins: ");
        while(obj.hasNextLine()){
            int num = obj.nextInt();
            ReturnNode result = ga.getSmallestNum(num);
            if(result == null){
                System.out.println("The smallest number of coins for change is: 0");
                System.out.println("The changed list is: []");
            }
            else {
                System.out.println("The smallest number of coins for change is: " + result.changeNum);
                System.out.println("The changed list is: "+ result.changeList.toString());
            }
        }
    }
}
