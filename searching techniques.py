'''linear_search'''
def linear_searc(harr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
        return -1
arr=list(map(int,input().split(",")))
target=int(input())
print(linear_search(arr,target))

'''binary_search'''

def binary_search(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+-1
        else:
            right=mid-1
    return -1
arr=[6,7,4,11]
target=7
print(binary_search(arr,target))