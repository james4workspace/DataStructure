

class LinkedList:
    class Node:
        '创建节点'

        def __init__(self, data):
            self.data = data
            self.next = None

    '创建列表'
    def __init__(self):
        '初始化列表'
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self,data):
        node = self.Node(data) #把Node实例化得到一个node对象
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def insert(self,position,data):
        cur = self.head
        cur_pos = 0
        if cur is None:
            raise Exception('The Linked List is empty')
        while cur_pos < position - 1:
            cur = cur.next
            if cur is None:
                raise Exception('List length less than index')
            cur_pos +=1

        node = self.Node(data)
        node.next = cur.next
        cur.next = node
        if node.next is None:
            self.tail = node

    def remove(self,position):
        cur = self.head
        cur_pos = 0
        if self.head is None:
            raise Exception('The Linked List is empty')
        while cur_pos < position - 1:
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_pos +=1
        if position == 0: # 删除头节点
            self.head = cur.next
            cur = cur.next
            return
        elif self.head is self.tail: #只有一个节点
            self.head = None
            self.tail = None
            return
        else:
            cur.next = cur.next.next
            if cur.next is None: # 删除节点是尾节点
                self.tail = cur

    def getSize(self):
        cur = self.head
        count = 0
        if cur is None:
            return count
        while cur is not None:
            count +=1
            cur = cur.next
        return count

    def search(self,item):
        cur = self.head
        found = False
        position = 0
        while cur is not None and not found:
            if cur.data == item:
                found = True
            else:
                cur = cur.next
                position +=1
        return found,position

if __name__ =='__main__':
    link_list = LinkedList()
    print(link_list.is_empty()) #判断为空
    for i in range(15):
        link_list.append(i)
    print(link_list.getSize()) #获得大小
    print(link_list.is_empty()) # 判断是否为空
    link_list.insert(0,1000) #插入元素
    print(link_list.getSize())
    link_list.remove(0)
    print(link_list.search(1000))

