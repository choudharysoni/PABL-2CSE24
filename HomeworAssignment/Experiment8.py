class Solution(object):
    def searchInsert(self, nums, target):
        left,right=0 ,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            
            elif nums[mid]<=target:
                left=mid +1

            else:
                right=mid-1


        return left  

obj=Solution()
nums=[1,3,5,6]
target=7
ans=obj.searchInsert(nums,target)
print(ans)


        