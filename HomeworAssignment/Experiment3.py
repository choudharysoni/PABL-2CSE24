class Solution:
    def kthsmallest(self,arr,k):
        arr.sort()
        return arr[k-1]
    

obj=Solution()
arr=[1,4,3,5,8,6]

k=4
result= obj.kthsmallest(arr,k)
print(result)