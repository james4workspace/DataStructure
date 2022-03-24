###########################################
"""
插入排序
"""

def insertionSort(arr,reverse = False):
    """
    插入排序
    时间复杂度：O(n**2)
    最糟糕情况：1+2+3+4+...+n -> n(n+1)/2
    空间复杂度：O(1)
    """
    if reverse is False:
        for i in range(1,len(arr),1):
            cur = arr[i]
            j = i -1
            while j>=0 and arr[j] >cur:
                # 与之前的数据进行比较
                arr[j+1] = arr[j]
                j-=1
            arr[j+1]=cur
    else:
        for i in range(1,len(arr),1):
            cur = arr[i]
            j = i -1
            while j>=0 and arr[j] >cur:
                # 与之前的数据进行比较
                arr[j+1] = arr[j]
                j-=1
            arr[j+1]=cur

    return arr
##################################################
def bubbleSort(arr,reverse=False):
    length = len(arr)
    arr = bubbleSortDetailed(arr,length,reverse)
    return arr

def bubbleSortDetailed(arr,length,reverse):
    change = False
    if reverse is False:      
        for i in range(1,length):
            if arr[i-1]>arr[i]: # 递增
                temp=arr[i]
                arr[i]=arr[i-1]
                arr[i-1]=temp
                change = True
    else:
        for i in range(1,length):
            if arr[i-1]<arr[i]: # 递减
                temp=arr[i]
                arr[i]=arr[i-1]
                arr[i-1]=temp
                change = True
    while change is True:
        length-=1
        arr,change = bubbleSortDetailed(arr,length,reverse)
    return arr,change



#################################################
def originalQuickSort(arr,reverse=False):
    arr = quickSort(arr,0,len(arr)-1,reverse)
    return arr

def quickSort(arr,left,right,reverse):
    """
    快速排序 Quick Sort
    时间复杂度：最糟糕：如果每次pivot只能放最左边，n + n-1 + n-2....+1 -> n(n+1)/2 -> O(n**2)
    空间复杂度：最糟糕：迭代n次，所以是O(n)
    正常情况，如果放中间位置，有logN level的空间复杂度，而每层排序n次，则为NlogN的复杂度。
    """
    if left>=right:
        return arr#即该array为空，或者只有一个元素
    if reverse is False:
        partition_index = ascendingPartition(arr,left,right) # 找到pivot，并且排好序，返回该pivot所在位置
    else:
        partition_index = descendingPartition(arr, left, right)  # 找到pivot，并且排好序，返回该pivot所在位置
    arr = quickSort(arr,left,partition_index-1,reverse)
    arr = quickSort(arr,partition_index+1,right,reverse)
    return arr

def swap(arr,left, right):
    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

def ascendingPartition(arr,left,right):
    pivot = arr[right] # 取最右边元素
    smaller_element_index = left # 记录比pivot小的index
    bigger_element_index = right-1 # 记录比pivot大的index
    while True:
        while smaller_element_index < right and arr[smaller_element_index] <= pivot:
            smaller_element_index+=1
        while bigger_element_index >=left and arr[bigger_element_index] > pivot:
            bigger_element_index -=1
        if smaller_element_index > bigger_element_index:
            # 如果两个index交叉，意味着算到头了
            break

        #如果两个循环被打破，自然就代表有大的在左边，小的在右边，互换就好
        swap(arr, smaller_element_index, bigger_element_index)

    # now smaller_element_index 是第一个比pivot大的元素
    swap(arr,smaller_element_index,right)
    return smaller_element_index

def descendingPartition(arr,left,right):
    pivot = arr[right] # 取最右边元素
    bigger_element_index = left # 记录比pivot大的index
    smaller_element_index = right-1 # 记录比pivot小的index
    while True:
        while bigger_element_index < right and arr[bigger_element_index] > pivot:
            bigger_element_index+=1
        while smaller_element_index >=left and arr[smaller_element_index] <= pivot:
            smaller_element_index -=1
        if smaller_element_index < bigger_element_index:
            # 如果两个index交叉，意味着算到头了
            break

        #如果两个循环被打破，自然就代表有大的在左边，小的在右边，互换就好
        swap(arr, bigger_element_index, smaller_element_index)

    # now bigger_element_index 是第一个比pivot小的元素
    swap(arr,bigger_element_index,right)
    return bigger_element_index

##################################################
def mergeSort(arr):
    """
    Merge Sorting : 归并排序
    大问题变成小问题逐个击破
    时间复杂度：切分的时候logN层，归并也是logN层，即2logN层，每层进行N个元素的排序，即2NlogN，去掉常数，即NlogN
    空间复杂度：因为需要Helper，所以空间复杂度即O(N)
    """
    helper = arr.copy()
    mergeSortDetailed(arr,helper,0,len(arr)-1)
    return arr

def mergeSortDetailed(arr,helper,start,end):
    if end-start<1:
        # 切分到子数组最后只有一个元素的时候为止
        return
    mid = (start+end)//2
    mergeSortDetailed(arr,helper,start,mid)
    mergeSortDetailed(arr,helper,mid+1,end)
    merge(arr,helper,start,mid,end)#先切分再合并

def merge(arr,helper,start,mid,end):
    for i in range(len(arr)):
        helper[i]=arr[i]
    left_start = start
    right_start = mid+1
    while left_start <= mid and right_start <=end:
        # 不越界的情况下
        if helper[left_start] <= helper[right_start]:
            # 左右小数组进行比较
            arr[start] = helper[left_start]
            start+=1
            left_start+=1
        else:
            arr[start] = helper[right_start]
            start+=1
            right_start+=1

    #结束后两种可能性：左边超界，右边超界
    if left_start <= mid:#右边超界，左边没超界
        while left_start <= mid:
            arr[start] = helper[left_start]
            start+=1
            left_start+=1
    else:
        # 左边超界，右边没超界
        while right_start <= end:
            arr[start] = helper[right_start]
            start +=1
            right_start+=1





import random
def randomList(start,end,length):
    length =int(abs(length)) if length else 0
    random_list = list()
    for i in range(length):
        random_list.append(random.randint(start,end))
    return random_list



if __name__ == "__main__":
    random_list = randomList(1,10,8)
    print("random list is {a}".format(a=random_list))
    #insertionSort(random_list)
    #originalQuickSort(random_list,reverse=True)
    #bubbleSort(random_list)
    mergeSort(random_list)
    print("sorted result: {a}".format(a=random_list))