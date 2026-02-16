class Solution:
    def largest(self, arr):
        largest=arr[0]

        for i in arr:
            if i>largest:
                largest=i


        return largest

obj=Solution()
arr= [1, 8, 7, 56, 90]
ans=obj.largest(arr)
print(ans)