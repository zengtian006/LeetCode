# Binary Search

用BS可以将时间复杂度降为O(logn)，一般用非递归的方式， 前提是数组是有序的，或者几乎有序：比如：'345612'

## 简单非递归模版

```python
def binarySearch(nums, target):
    left, right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1
```

## 变体

1. 找到某个元素第一次出现的位置

```python
def binarySearch(nums, target):
    left, right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid] == target:
            if mid == 0 or nums[mid-1]!=target:
                return mid
            else:
                right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1
```

2. 找到某元素最后一次出现的位置

```python
def binarySearch(nums, target):
    left, right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid] == target:
            if mid == len(nums)-1 or nums[mid+1]!=target:
                return mid
            else:
                left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1
```

3. 找到第一個大于等于某元素的位置

第一种写法

```python
def binarySearch(nums, target):
    left, right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid] >= target:
            if mid == 0 or nums[mid-1]<target:
                return mid
            else:
                right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1
```

第二种写法
```python
def binarySearch(nums, target):
    left, right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid] >= target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return right + 1 
```

4. 找到最后一个小于等于某元素的位置

第一种写法

```python
def binarySearch(nums, target):
    left, right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid] <= target:
            if mid == len(nums)-1 or nums[mid+1]>target:
                return mid
            else:
                left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
    return -1
```

第二种写法

```python
def binarySearch(nums, target):
    left, right = 0, len(nums)-1
    while left<=right:
        mid = left + (right-left)//2
        if nums[mid] <= target:
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
    return left - 1
```

[Bianry Serach Leetcode 练习题](https://github.com/zengtian006/LeetCode/tree/master/Binary%20Search)