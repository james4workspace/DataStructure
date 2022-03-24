class ArrayStack:
    """
    Sequential Stack Implementation
    """

    def __init__(self):
        """
        Initialize an empty stack, __stack means it's a private member
        """
        self.__stack = list()

    def top(self):
        """
        get the top element of stack
        return: if stack is empty return None, else return the top element
        """
        return None if self.isEmpty() else self.__stack[-1]

    def push(self,obj):
        self.__stack.append(obj)

    def pop(self):
        return None if self.isEmpty() else self.__stack.pop()

    def clear(self):
        """
        clear the whole stack
        """
        self.__stack.clear()

    def isEmpty(self):
        return len(self.__stack) == 0

    def length(self):
        return len(self.__stack)

