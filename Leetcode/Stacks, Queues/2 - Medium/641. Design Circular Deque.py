class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.ls = [-1]*k
        self.size = 0
        self.front = 0
        self.last = 0
    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.ls[self.front] = value
        else:
            self.front = (self.front-1)%len(self.ls)
            self.ls[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.ls[self.last] = value
        else:
            self.last = (self.last+1)%len(self.ls)
            self.ls[self.last] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.ls[self.front] = -1
        self.front = (self.front+1)%len(self.ls)
        self.size -= 1
        if self.isEmpty():
            self.front = self.last = 0
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.ls[self.last] = -1
        self.last = (self.last-1)%len(self.ls)
        self.size-=1
        if self.isEmpty():
            self.front = self.last = 0
        return True
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.ls[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.ls[self.last]
        
    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size==0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.ls)==self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()