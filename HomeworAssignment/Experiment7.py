class Solution:
    def maxSubarraySum(self, arr):
        currentsum=arr[0]
        maxsum=arr[0]

        for i in range(1,len(arr)):
            if currentsum + arr[i]> arr[i]:
                currentsum = currentsum + arr[i]

            else:
                currentsum= arr[i]

            if currentsum > maxsum:
                maxsum = currentsum

        return maxsum

obj=Solution()
arr=[2, 3, -8, 7, -1, 2, 3]
ans=obj.maxSubarraySum(arr)
print(ans) 