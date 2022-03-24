class ArrayQueue:
    """
    Sequential Array Queue Implementation

    """
    def __init__(self):
        self.__queue = list()

    def enqueue(self,data):
        """add a new item to the array queue"""
        self.__queue.append(data)

    def dequeue(self):
        self.__queue.pop(0)

    def peek(self):
        return self.__queue[0]

    def isEmpty(self):
        return self.__queue ==[]





