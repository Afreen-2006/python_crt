'''leetcode problem on move zeroes ide version'''
def movezeroes(nums):
    x=[]
    y=[]
    for i in range(len(nums)):
        if nums[i]:
            x.append(nums[i])
        else:
            y.append(nums[i])
    z=x+y
    print(z)
nums=[0,1,2,0,3,6]
movezeroes(nums)

'''leetcode version'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[idx]=nums[i]
                idx+=1
        for j in range(idx,len(nums)):
            nums[j]=0