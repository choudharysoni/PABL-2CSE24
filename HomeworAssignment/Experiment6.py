class Solution:
    def rotate(self, arr):
        last=arr[-1]

        for i in range(len(arr)-1,0,-1):
            arr[i]=arr[i-1]
        arr[0]=last

        return arr

obj=Solution()
arr=[9, 8, 7, 6, 4, 2, 1, 3]
ans=obj.rotate(arr)
print(ans)    