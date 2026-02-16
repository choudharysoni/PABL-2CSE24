class Solution:
    def kthSmallest(self, arr, k):
        arr.sort()
        return arr[k - 1]


obj = Solution()
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
k = 4

ans = obj.kthSmallest(arr, k)
print(ans)