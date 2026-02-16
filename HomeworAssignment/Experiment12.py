class Solution:
    def getMinDiff(self, arr, n, k):

        if n == 1:
            return 0

        arr.sort()

        ans = arr[n - 1] - arr[0]

        smallest = arr[0] + k
        largest = arr[n - 1] - k

        for i in range(n - 1):

            min_height = min(smallest, arr[i + 1] - k)
            max_height = max(largest, arr[i] + k)

            if min_height < 0:
                continue

            ans = min(ans, max_height - min_height)

        return ans


obj = Solution()

k = 2
arr = [1, 5, 8, 10]
n = len(arr)

print(obj.getMinDiff(arr, n, k))