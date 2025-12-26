'''leetcode two sums'''

def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
              return i,j 
print(twosum([9,7,8,2,54],9))