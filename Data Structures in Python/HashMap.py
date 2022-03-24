class HashNode:
    def __init__(self,key,value):
        self.key=key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self,num):
        self.num=num # list的固定长度
        self.size =0 #一共有多少个值插入
        self.hash_table=self.createBucket()

    def createBucket(self):
        """
        生成固定长度的list，用来作为hash table的存放地址
        """
        hash_table = [None for i in range(self.num)]
        return hash_table

    def getBucketIndex(self,key):
        """
        :param key: int: 其key值
        :return index: int: 其key值在Hash Table这个array里的位置
        """
        hash_code=self.hashFunction(key)#首先得到从哈希函数中获得的键值
        index = hash_code % self.num #再通过取余数获得位置index
        return index

    def hashFunction(self,key):
        """
        :param key: int
        :return hash_code: int
        """
        hash_code = hash(key) #这里使用的是默认的哈希函数，也可以自己调整
        return hash_code

    def add(self,key,value):
        """
        :param key: int
        :param value: int
        :return: boolean
        核心方法：如何处理输入的数据，value是具体数据
        """
        bucket_index = self.getBucketIndex(key)
        head = self.hash_table[bucket_index] #获得头节点
        # 判断头节点是否为空，空则直接插入，非空则判断是否为key，是则修改数据
        while head:
            if head.key ==key:
                head.value = value
                return True
            else:
                head = head.next
        # 循环结束也没有找到匹配的值，或头结点为空，则插入新节点
        else:
            head = self.hash_table[bucket_index]
            new_node = HashNode(key,value)
            new_node.next = head
            self.hash_table[bucket_index] = new_node
            self.size+=1

        # 假如Array填满，需要更多的Array空间的话
        if self.size >=self.num:
            self.generateBiggerArray()

        return True

    def generateBiggerArray(self):
        """
        获得更大的array，将现有节点移动到bigger array里
        """
        temp = self.hash_table
        self.num = self.num * 2
        self.hash_table=self.createBucket()
        for each_head in temp:
            while each_head:
                self.add(each_head.key,each_head.value)
                each_head = each_head.next

    def get(self,key):
        """
        :param key: int
        :return: value: int or None
        """
        hash_index = self.getBucketIndex(key)
        head = self.hash_table[hash_index]
        while head:
            if head.key == key:
                return head.value
            else:
                head = head.next

        return None

    def getSize(self):
        return self.size

    def remove(self,key):
        hash_index = self.getBucketIndex(key)
        head = self.hash_table[hash_index]
        prev = None
        while head:
            if head.key == key:
                break
            prev = head
            head = head.next

        if head is None:
            return None

        if prev is not None:
            # head 不是头节点
            prev.next = head.next
        else:
            # head是头结点
            self.hash_table[hash_index]=head.next

        self.size -=1

        return head.value


def addAll(hm,key_list, value_list):
    for i in range(len(key_list)):
        hm.add(key_list[i],value_list[i])

def printAll(hm,key_list):
    for each in key_list:
        print(each,hm.get(each))

if __name__ =="__main__":
    key_list = [num for num in range(100)]
    value_list=[num for num in range(99,-1,-1)]
    hm = HashMap(20)
    addAll(hm,key_list,value_list)
    printAll(hm,key_list)

