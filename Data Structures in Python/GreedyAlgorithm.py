import sys
import heapq

def getSmallestNum(coin_choices,sum_num):
    """
    这里我们使用贪心算法，每一步都选择最大的Coin，直到最终值大于或等于sum_num，再退回去选择小的Coin
    :param sum_num: int
    :return: list
    """
    if sum_num ==0:
        return []
    coin_choices = [-each for each in coin_choices]
    heapq.heapify(coin_choices)
    ans = list()
    sum_sofar=0 # memoize no need to sum every turn
    ans = countSum(ans,sum_sofar,sum_num,coin_choices)
    return ans

def countSum(ans,sum_sofar,sum_num,coin_choices):
    max_num = -(heapq.heappop(coin_choices))
    while sum_sofar <sum_num:
        ans.append(max_num)
        sum_sofar +=max_num
    if sum_sofar == sum_num:
        return ans
    else:
        ans.pop()
        sum_sofar-=max_num
        ans = countSum(ans, sum_sofar, sum_num, coin_choices)
        return ans

if __name__=="__main__":
    print("Please Enter the SUM for calcualtion:")
    sum_num = int(sys.stdin.readline())
    coin_choices = [50,20,10,5,2,1]
    coins = getSmallestNum(coin_choices, sum_num)
    print(coins)
    print("the smallest number of coins is: {}".format(len(coins)))
