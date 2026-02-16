class Solution:
    def merge(self, a, b, n, m):

        def nextGap(gap):
            if gap <= 1:
                return 0
            return (gap // 2) + (gap % 2)

        gap = nextGap(n + m)

        while gap > 0:
            i = 0
            j = gap

            while j < n + m:

                if i < n:
                    left = a[i]
                else:
                    left = b[i - n]

                if j < n:
                    right = a[j]
                else:
                    right = b[j - n]

                if left > right:
                    if i < n and j < n:
                        a[i], a[j] = a[j], a[i]
                    elif i < n and j >= n:
                        a[i], b[j - n] = b[j - n], a[i]
                    else:
                        b[i - n], b[j - n] = b[j - n], b[i - n]

                i += 1
                j += 1

            gap = nextGap(gap)
obj = Solution()

a = [2, 4, 7, 10]
b = [2, 3]

obj.merge(a, b, len(a), len(b))

print(a)
print(b)