class MaxHeap:
    """
    因为堆的特殊性，这里可以直接用数组来实现，而非链表
    """
    def __init__(self):
        #self.capacity = capacity # 容量，存节点数量，但因为python的list是无限容量的，所以不需要capacity
        self.size = 0 # 当前节点数量
        self.array = list() # 存当前节点的数组


    """
    接下来是获得各个节点的index
    """
    def getLeftChildIndex(self,parentIndex):
        """
        通过计算获得孩子的节点
        """
        return 2*parentIndex +1

    def getRightChildIndex(self,parentIndex):
        return 2*parentIndex.key +2

    def getParentIndex(self,childIndex):
        return (childIndex-1)//2#底板除

    def hasLeftChild(self,index:int):
        return self.getLeftChildIndex(index)<self.size

    def hasRightChild(self,index):
        return self.getLeftChildIndex(index)<self.size

    def hasParent(self,index):
        return (index - 1) // 2 >=0 # 底板除

    """
    接下来是取得节点的值
    """
    def getLeftChildValue(self, parentIndex):
        return self.array[self.getLeftChildIndex(parentIndex)]

    def getRightChildValue(self, parentIndex):
        return self.array[self.getRightChildIndex(parentIndex)]

    def getParentValue(self,childIndex):
        return self.array[self.getParentIndex(childIndex)]

    """
    接下来是各种直接对heap的操作
    """

    def insert(self,item):
        self.array.append(item)
        self.size+=1
        self.heapifyUp()


    def heapifyUp(self):
        index = self.size - 1 #因为在insert里size永远在插入之后加1，所以size比index大1
        while self.hasParent(index) and self.getParentValue(index) < self.array[index]:
            self.swap(self.getParentIndex(index),index)#互换
            index = self.getParentIndex(index)#更新子节点

    def swap(self,parentIndex,childIndex):
        temp = self.array[parentIndex]
        self.array[parentIndex] = self.array[childIndex]
        self.array[childIndex] = temp

    def poll(self):
        """
        移除根节点，把最大数移到根节点处
        """
        if self.size == 0:
            return
        element = self.array[0]
        self.array[0]=self.array[self.size-1]#将最后输入的数字放到根节点
        self.size -=1
        self.heapifyDown()


    def heapifyDown(self):
        index =0
        while self.hasLeftChild(index):
            largerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.getRightChildValue(index) > self.getLeftChildValue(index):
                largerChildIndex = self.getRightChildValue(index)

            if self.array[index] < self.array[largerChildIndex]:
                self.swap(index, largerChildIndex)
            else:
                break

            index = largerChildIndex

    def peek(self):
        if self.size ==0:
            return
        else:
            return self.array[0]


