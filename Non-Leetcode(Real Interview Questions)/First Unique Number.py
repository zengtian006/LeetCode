# You have a queue of integers, you need to retrieve the first unique integer in the queue.

# Implement the FirstUnique class:

# FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
# int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
# void add(int value) insert value to the queue.
 
# Example 1:

# Input: 
# ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
# [[[2,3,5]],[],[5],[],[2],[],[3],[]]
# Output: 
# [null,2,null,2,null,3,null,-1]

# Explanation: 
# FirstUnique firstUnique = new FirstUnique([2,3,5]);
# firstUnique.showFirstUnique(); // return 2
# firstUnique.add(5);            // the queue is now [2,3,5,5]
# firstUnique.showFirstUnique(); // return 2
# firstUnique.add(2);            // the queue is now [2,3,5,5,2]
# firstUnique.showFirstUnique(); // return 3
# firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
# firstUnique.showFirstUnique(); // return -1

# Example 2:

# Input: 
# ["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
# [[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
# Output: 
# [null,-1,null,null,null,null,null,17]

# Explanation: 
# FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
# firstUnique.showFirstUnique(); // return -1
# firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
# firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
# firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
# firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
# firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
# firstUnique.showFirstUnique(); // return 17

# Example 3:

# Input: 
# ["FirstUnique","showFirstUnique","add","showFirstUnique"]
# [[[809]],[],[809],[]]
# Output: 
# [null,809,null,-1]

# Explanation: 
# FirstUnique firstUnique = new FirstUnique([809]);
# firstUnique.showFirstUnique(); // return 809
# firstUnique.add(809);          // the queue is now [809,809]
# firstUnique.showFirstUnique(); // return -1

class Node:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None
        
class Dll:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.count = 0
        
    def insert(self, val):
        node = Node(val)
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre.next = node
        self.tail.pre = node
        self.count += 1
        return node
    
    def remove(self, node):
        pre = node.pre
        nxt = node.next
        node.pre.next = nxt
        node.next.pre = pre
        self.count -= 1
    
    def isEmpty(self):
        return self.count == 0
    
    
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dll = Dll()
        self.dic = {}
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        return self.dll.head.next.val

    def add(self, value: int) -> None:
        if value not in self.dic:
            self.dic[value] = self.dll.insert(value)
        elif value in self.dic and self.dic[value] != -1:
            self.dll.remove(self.dic[value])
            self.dic[value] = -1