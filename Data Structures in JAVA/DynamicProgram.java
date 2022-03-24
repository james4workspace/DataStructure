package DataStructure;

import java.util.Scanner;
public class DynamicProgram {
    int countTime = 0;

    public int fib(int n){
        /*正常的递归函数，通过反复递归得到最终值
        * 其运算时间复杂度 Time Complexity: 2^n
        * */
        int result;
        if(n==1 || n==2){
            result = 1;
            return result;
        }
        result = fib(n-1)+fib(n-2);
        countTime +=1;
        System.out.println("process "+countTime+": fib("+n+") = fib("+(n-1)+") + fib("+(n-2)+")");
        return result;
    }
    private void resetCount(){
        this.countTime = 0;
    }

    public int fibBottomUp(int n){
        /*通过存储，每个数据只需要计算一次，存储后直接调用即可
        * 动态规划的特点在于：
        *   1. recursion: 主要针对recursive method进行改进;
        *   2. memoize: 通过存储临时数据，达到空间换时间；
        *   3. bottom up: 比起正常的逻辑从问题直接开始解决，选择从最底层开始往上解决；
        * 其运算时间复杂度 Time Complexity: O(n)
        * */
        int[] fibList = new int[n];//利用该列表，达到存储临时数据的目的
        fibList[0]=1;
        fibList[1]=1;
        for(int i=2;i<n;i++){
            //这里通过bottom up的方式，从底层开始计算，保证每个数字只计算一次
            fibList[i]=fibList[i-1]+fibList[i-2];
            countTime+=1;
            System.out.println("process "+countTime+": fib("+(i+1)+") = fib("+i+") + fib("+(i-1)+")");
        }
        return fibList[n-1];
    }

    public static void main(String[] args){
        /*测试代码*/
        Scanner obj = new Scanner(System.in);
        DynamicProgram dp = new DynamicProgram();
        System.out.printf("Please enter the position of fib series you wanna count: ");
        while(obj.hasNextLine()){
            int n = obj.nextInt();
            System.out.println("1. It's using the dynamic programming function below:");
            dp.resetCount();//重置countTime
            int result = dp.fibBottomUp(n);
            System.out.println("the result is: "+result);

            System.out.println("2. It's using the original recursive function below:");
            dp.resetCount();//重置countTime
            result = dp.fib(n);
            System.out.println("the result is: "+result);
        }
    }
}
