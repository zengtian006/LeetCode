class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1=collections.deque()
        self.q2=collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.q2:
            self.q2.append(x)
        else:
            self.q1.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        
        if self.q1:
            return self.switch(self.q1, self.q2)
        else:
            return self.switch(self.q2, self.q1)
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.q1:
            x = self.switch(self.q1, self.q2)
            self.q2.append(x)
            return x
        else:
            x = self.switch(self.q2, self.q1)
            self.q1.append(x)
            return x
        
    def switch(self, q1, q2):
        while len(q1)>1:
            q2.append(q1.popleft())
        return q1.popleft()

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.q1 and not self.q2