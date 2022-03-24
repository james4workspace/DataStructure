class StackNode:
    """
    Create Node
    """
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.top = None

    def push(self,obj):
        node = StackNode(obj)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return

        self.top = self.top.next
        return

    def peek(self):
        if self.top is None:
            print("Stack is Empty")
            return False
        else:
            return self.top.data

    def isEmpty(self):
        return self.top == None

    def showAll(self):
        cur = self.top
        listAll= list()
        if self.top is None:
            return
        else:
            while cur is not None:
                listAll.append(cur.data)
                cur = cur.next
        return listAll

def easyAppend(stack_name,input_list):
    for each in input_list:
        stack_name.push(each)

if __name__ =="__main__":
    stack1 = LinkedListStack()
    input_list=[1,3,2,4,5,3,2,44,3,1000]
    easyAppend(stack1, input_list)
    print(stack1.showAll())



