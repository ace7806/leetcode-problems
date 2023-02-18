Nums = [1,1,2,2,3,3.2,4,4,4.5] # = 4
Nums2 = [1,3,5] # = 2
Nums3 = [-4,-3,-2,-1]# = 2
'''
assuming its sorted
Nums = [1,1,2,2,3,3,4,4,4]
we have left and right pointer starting at 0
if right elem - left elem has a difference less than 1, then move right pointer up and calculate maxLen
else move left pointer up till difference meets requirement, then calculate maxLen
'''
def longestSubstringBy1(nums):
    l=0
    maxLen = 0
    for r in range(len(nums)):
        while nums[r]-nums[l] >1: l+=1
        maxLen = max(maxLen, r-l+1)
    return maxLen
print(longestSubstringBy1(Nums))
print(longestSubstringBy1(Nums2))
print(longestSubstringBy1(Nums3))