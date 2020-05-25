# For a given list of integers and integer K, find the number of non-empty subsets S such that min(S) + max(S) <= K.

# Example 1:

# nums = [2, 4, 5, 7]
# k = 8
# Output: 5
# Explanation: [2], [4], [2, 4], [2, 4, 5], [2, 5]
# Example 2:

# nums = [1, 4, 3, 2]
# k = 8
# Output: 15
# Explanation: 16 (2^4) - 1 (empty set) = 15
# Example 3:

# nums = [2, 4, 2, 5, 7]
# k = 10
# Output: 27
# Explanation: 31 (2^5 - 1) - 4 ([7], [5, 7], [4, 5, 7], [4, 7]) = 27

def countSubsets(nums,k):
    nums.sort()
    count = 0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+nums[j]>k:
                break
            if nums[i]+nums[j]<=k:
                count += 2**((j-i-1) if j-i>1 else 0)
    print(count)
    return count

countSubsets([2, 4, 5, 7], 8)
countSubsets([1,2,3,4], 8)
countSubsets([2, 4, 2, 5, 7], 10)


# 当 nums[i] +nums[j] <k时,  符合要求的组合就是 i到j以内数字的所有集合 append nums[i] 和 nums[j] 
# 比如[2, 4, 5, 7], k=8 : i=0,j =2 subsets = [2,5] [2,4,5]
# 比如[1,2,3,4], k=8 :   i=0, j=3 subsets =[1,4], [1,2,4],[1,2,3,4] [1,3,4]
# 当i=j subset 就是 一个数字 【nums[i]]
