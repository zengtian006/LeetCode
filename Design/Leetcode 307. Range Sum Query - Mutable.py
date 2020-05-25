class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.left = None
        self.right = None

class NumArray:

    def __init__(self, nums: List[int]):
        self.root = self.buildTree(nums, 0, len(nums)-1)
        
    def buildTree(self, nums, start, end):
        if start>end:
            return None
        
        if start == end:
            node = Node(start, end)
            node.total = nums[start]
            return node
        
        root = Node(start, end)
        
        mid = start + (end-start)//2
        
        root.left = self.buildTree(nums, start, mid)
        root.right = self.buildTree(nums, mid+1, end)
        root.total = root.left.total + root.right.total
        return root

    def update(self, i: int, val: int) -> None:
        return self.updateHelper(self.root, i, val)
    
    def updateHelper(self, root, i ,val):
        if root.start == root.end == i:
            root.total = val
            return val
        
        mid = root.start +(root.end-root.start)//2
        if i<=mid:
            self.updateHelper(root.left, i, val)
        else:
            self.updateHelper(root.right, i, val)
        
        root.total = root.left.total + root.right.total
        return root.total

    def sumRange(self, i: int, j: int) -> int:
        return self.sumRangeHelper(self.root, i, j)
    
    def sumRangeHelper(self, root, i, j):
        if root.start ==i and root.end ==j:
            return root.total
        
        mid = root.start + (root.end-root.start)//2
        if j<=mid:
            return self.sumRangeHelper(root.left, i, j)
        elif i>=mid+1:
            return self.sumRangeHelper(root.right, i, j)
        else:
            return self.sumRangeHelper(root.left, i, mid)+ self.sumRangeHelper(root.right, mid+1, j)