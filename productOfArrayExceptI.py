test = [3,6,3]
'''
1 2 3 4 = 24 12 8 6

1 1 2 6

24 12 4 1

24 12 8 1
'''

def productOfArrayExceptI(nums):
       n = len(nums)
       if n<=1:return nums
       leftProductSubArr = [1]*n
       rightProductSubArr = [1]*n
       for i in range(1,n): leftProductSubArr[i] = nums[i-1]*leftProductSubArr[i-1] 
       for i in range(n-2,-1,-1): rightProductSubArr[i] = nums[i+1]*rightProductSubArr[i+1] 
       for i in range(n): leftProductSubArr[i] *= rightProductSubArr[i]
       return leftProductSubArr
print(productOfArrayExceptI(test))