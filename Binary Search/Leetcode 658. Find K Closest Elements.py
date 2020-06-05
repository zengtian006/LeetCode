class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr)-k-1
        while left <= right:
            mid = left + (right-left)//2
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid - 1
        return arr[left:left+k]