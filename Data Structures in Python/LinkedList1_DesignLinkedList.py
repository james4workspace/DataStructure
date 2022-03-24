class MyLinkedList:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.next = None
        self.count = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        cur_idx = 0
        cur = self.head
        if cur is None:
            return -1
        while cur_idx <index:
            if cur.next is None:
                return -1
            cur = cur.next
            cur_idx +=1
        return cur.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        # firstly, estimate whether it's empty linked list or not
        if self.count == 0:
            node = self.Node(val)
            self.head = node
            self.tail = node
        else: # then insert the node into the linked list
            node = self.Node(val)
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.count +=1


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        # firstly, estimate whether it's empty linked list or not
        if self.count == 0:
            node = self.Node(val)
            self.head = node
            self.tail = node
        else:  # then insert the node into the linked list
            node = self.Node(val)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.count += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        # if the linked list is empty
        if self.count ==0 and index ==0:
            node = self.Node(val)
            self.head = node
            self.tail = node
            self.count +=1
            return
        if self.count <index:
            raise Exception('the index is longer than the length of linked list, therefore, the insertion is impossible')
        elif self.count == index:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            cur_idx = 0
            while cur_idx < index-1:
                cur = cur.next
                cur_idx+=1
            node = self.Node(val)
            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
            cur.next = node
            self.count +=1




    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        cur = self.head
        cur_idx =0
        if self.count ==0:
            # the linked list is empty
            return
        elif self.count < index+1:
            return
        else:
            if self.count == index+1 and index == 0:
                self.head = None
                self.tail = None
                self.count -=1
                return

            elif index ==0: # delete the head
                self.head = cur.next
                self.head.prev = None
                self.count -= 1
                return
            elif index+1 == self.count:
                self.tail = self.tail.prev
                self.tail.next = None
                self.count -= 1
                return
            else:
                while cur_idx < index:
                    cur = cur.next
                    cur_idx+=1
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                self.count -= 1
                return

    def getAll(self):
        cur = self.head
        listAns = list()
        for i in range(self.count):
            listAns.append(cur.val)
            cur = cur.next
        print(listAns)

if __name__ =='__main__':
    myLinkedList = MyLinkedList()
    myLinkedList.addAtHead(7)
    myLinkedList.addAtHead(2)
    myLinkedList.addAtHead(1)
    myLinkedList.getAll()
    myLinkedList.addAtIndex(3, 0)
    myLinkedList.deleteAtIndex(2)
    myLinkedList.addAtHead(6)
    myLinkedList.addAtTail(4)
    print(myLinkedList.get(4))
    myLinkedList.getAll()
    myLinkedList.addAtHead(4)
    myLinkedList.addAtIndex(5, 0)
    myLinkedList.addAtHead(6)
    myLinkedList.getAll()

