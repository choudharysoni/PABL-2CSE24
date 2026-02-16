class Solution:
    def minJumps(self, arr, n):

        if n == 1:
            return 0

        if arr[0] == 0:
            return -1

        jumps = 1
        steps_left = arr[0]
        farthest = arr[0]

        for i in range(1, n):

            if i == n - 1:
                return jumps

            if i + arr[i] > farthest:
                farthest = i + arr[i]

            steps_left -= 1

            if steps_left == 0:
                jumps += 1

                if i >= farthest:
                    return -1

                steps_left = farthest - i

        return -1


obj=Solution()
arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n=len(arr)
ans=obj.minJumps(arr,n)
print(ans)