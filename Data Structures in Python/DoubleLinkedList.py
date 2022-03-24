import math
class DoubleLinkedList(object):
    class Node:
        def __init__(self,val):
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.head is not None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if self.head is None or index>= self.size:
            return -1
        if index < math.ceil(self.size/2):
            current = self.getNodeFHead(index)
        else:
            current = self.getNodeFTail(self.size - index-1)
        return current.val

    def getNodeFHead(self,index):
        """
        :type index: int
        :return current: Node
        """
        current = self.head
        if index == 0:
            return current
        for i in range(index):
            current = current.next
            if current is None:
                return None
        return current

    def getNodeFTail(self,index):
        """
        :type index: int
        :return current: Node
        """
        current = self.tail
        if index == 0:
            return current
        for i in range(index):
            current = current.prev
            if current is None:
                return None
        return current



    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.size += 1
        if self.head is None:
            self.head = self.Node(val)
            self.tail = self.head
            return
        new_node = self.Node(val)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        return True

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.size += 1
        if self.head is None:
            self.head = self.Node(val)
            self.tail = self.head
            return
        new_node =self.Node(val)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        return True

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # 四种情况：加在头，加在尾，加超了，加在中间
        if index == 0:
            self.addAtHead(val)
            return True
        if index == self.size:
            self.addAtTail(val)
            return True
        if index > self.size:
            return False
        if index < math.ceil(self.size/2):
            current = self.getNodeFHead(index)
        else:
            current = self.getNodeFTail(self.size - index-1)
        new_node = self.Node(val)
        new_node.prev = current.prev
        current.prev.next = new_node
        current.prev = new_node
        new_node.next = current
        self.size +=1
        return True


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        分以下情况：LinkedList 为空，index为0，index为tail_index, index在中间，index超过范围
        """
        if self.head is None:
            return False
        if index > self.size-1:
            # 超出范围
            return False
        if index == 0:
            # 首位
            if self.head.next is not None:
                self.head.next.prev = None
            self.head = self.head.next
            self.size-=1
            return True
        elif index == self.size-1:
            # 尾巴
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.size-=1
            return True
        # 接下来是删中间
        if index < math.ceil(self.size/2):
            current = self.getNodeFHead(index)
        else:
            current = self.getNodeFTail(self.size - index-1)
        prev_node = current.prev
        next_node = current.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size-=1
        return True

    def getHead(self):
        return self.head

    def getAll(self):
        cur = self.head
        list_ans = list()
        for i in range(self.size):
            list_ans.append(cur.val)
            cur = cur.next
        print(list_ans)

if __name__ =='__main__':
    myLinkedList = DoubleLinkedList()
    myLinkedList.addAtHead(7)
    myLinkedList.addAtHead(2)
    myLinkedList.addAtHead(1)
    myLinkedList.getAll()
    myLinkedList.addAtIndex(3, 0)
    myLinkedList.getAll()
    myLinkedList.deleteAtIndex(2)
    myLinkedList.getAll()
    myLinkedList.addAtHead(6)
    myLinkedList.addAtTail(4)
    myLinkedList.getAll()
    print(myLinkedList.get(4))
    myLinkedList.addAtHead(4)
    myLinkedList.addAtIndex(5, 0)
    myLinkedList.addAtHead(6)
    myLinkedList.getAll()
    print(myLinkedList.head.val)
    list1 = myLinkedList.head # 获得头节点，脱离类范围
    print(list1.next.val)