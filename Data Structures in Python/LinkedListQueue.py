class QueueNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListQueue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self,data):
        new_node = QueueNode(data)
        if self.front is None: # 判断是否为空
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("the queue is empty")
        else:
            self.front = self.front.next
            if self.front == None:
                self.rear = None

    def isEmpty(self):
        return self.front is None

    def showAll(self):
        cur = self.front
        listAll = list()
        if self.front is None:
            return
        else:
            while cur is not None:
                listAll.append(cur.data)
                cur = cur.next
        return listAll

def easyAppend(queue_name,input_list):
    for each in input_list:
        queue_name.enqueue(each)

if __name__ =="__main__":
    queue1 = LinkedListQueue()
    input_list=[1,3,2,4,5,3,2,44,3,1000]
    easyAppend(queue1, input_list)
    print(queue1.showAll())
    queue1.dequeue()
    print(queue1.showAll())

