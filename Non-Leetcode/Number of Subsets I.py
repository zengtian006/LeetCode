# For a given list of integers and integer K, find the number of non-empty subsets S such that min(S) + max(S) = K.

# Example 1:

# nums = [1, 2, 3, 4]
# k = 5
# Output: 5
# Explanation: [1,4],[1,2,4][1,2,3,4][1,3,4][2,3]

def countSubsets(nums,k):
    nums.sort()
    count = 0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+nums[j]>k:
                break
            if nums[i]+nums[j]==k:
                count += 2**((j-i-1) if j-i>1 else 0)
    print(count)
    return count

countSubsets([1,2,3,4,5], 5)