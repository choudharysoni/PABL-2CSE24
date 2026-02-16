class Solution:
    def isSubset(self, a, b):

        freq = {}

        for x in a:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        for y in b:
            if y not in freq or freq[y] == 0:
                return False
            freq[y] -= 1

        return True


obj = Solution()

a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]

print(obj.isSubset(a, b))