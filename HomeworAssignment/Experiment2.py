class Solution:
    def minMaxElement(self,arr):
        min=arr[0]
        max=arr[0]

        for i in arr:
         if i<min:
            min=i

         if i>max:
            max=i

        return[min,max]




obj=Solution()
arr = [1, 4, 3, 5, 8, 6]
result=obj.minMaxElement(arr)


print("Min Element:", result[0])
print("Max Element:", result[1])
