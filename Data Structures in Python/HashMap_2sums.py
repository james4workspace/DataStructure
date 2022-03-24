class Solution1:
    def twoSum(self, nums, target):
        """
        这是一个很典型的等差数列求和的时间复杂度，其复杂度为n**2，不符合题目要求
        """
        limit = len(nums)
        for i in range(limit):
            f = 1
            while f <= limit - i-1:
                if (nums[i] + nums[i+f]) == target:
                    return [i, i+f]
                else:
                    f+=1
        return None


class Solution2:
    """
    哪怕Test结果正确，但实验结果是报错的，说明代码本身健壮性不足，需要更多的测试和Debug，对于Easy类题目来说不合适
    """
    def __init__(self):
        self.hash_table = None

    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None

    def twoSum(self, nums, target) :
        new_nums = list()
        for each in nums:
            new_nums.append(abs(each))
        size = max(new_nums) +1
        self.hash_table = self.createBucket(size)
        lenght = len(self.hash_table)
        for i in range(len(nums)):
            self.add(key=nums[i], value=i, target=target)

        result = self.judge()
        return result

    def createBucket(self, size):
        return [None for i in range(size)]

    def getIndex(self, key, target):
        index1 = abs(target - key)
        index2 = key
        if len(self.hash_table) - 1 < index1:
            return None, index2
        else:
            return index1, index2

    def add(self, key, value, target):
        index1, index2 = self.getIndex(key, target)
        if index1 is None:
            return False
        else:
            head = self.hash_table[index1]
            new_node = self.Node(key, value)
            new_node.next = head
            self.hash_table[index1] = new_node

            head = self.hash_table[index2]
            new_node.next = head
            self.hash_table[index2] = new_node
            return True

    def judge(self):
        for each_head in self.hash_table:
            if each_head is not None:
                while each_head.next is not None:
                    if each_head.value != each_head.next.value:
                        if each_head.value > each_head.next.value:
                            return [each_head.next.value, each_head.value]
                        else:
                            return [each_head.value, each_head.next.value]
                    else:
                        each_head = each_head.next
        return [None, None]

class Solution3:

    def twoSum(self, nums, target) :
        list_count = list()
        for i in range(len(nums)):
            if (target - nums[i]) not in list_count:
                # 如果其另一半不在列表中，证明到目前为止尚未录入列表，则直接录入
                list_count.append(nums[i])
            else:
                # 如果在列表中，则证明找到了，把这一半的位置调出来，再把原来的位置i也调出即可
                pos1=list_count.index((target-nums[i]))
                pos2=i
                return [pos1,pos2]




class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_com = dict()
        for i in range(len(nums)):
            if nums[i] in dict_com.keys():
                return [dict_com[nums[i]],i]
            else:
                dict_com[target - nums[i]] = i




if __name__ == '__main__':
    nums = [2,7,11,15,-3,-123,20,13,-15,22]
    target = 0
    s = Solution3()
    print(s.twoSum(nums, target))

