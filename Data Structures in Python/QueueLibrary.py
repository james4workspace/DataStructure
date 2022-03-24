import queue
customers = queue.PriorityQueue() #we initialise the PQ class instead of using a function to operate upon a list.
customers.put((2, "Harry"))
customers.put((3, "Charles"))
customers.put((1, "Riya"))
customers.put((4, "Stacy"))
while customers.empty() is not True:
     print(customers.get())
     #Will print names in the order: Riya, Harry, Charles, Stacy.

import queue


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        que = queue.PriorityQueue()
        for each in nums:
            que.put(-each)

        for i in range(k):
            result = que.get()
        result = -result
        return result