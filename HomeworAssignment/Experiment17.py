class Solution:
    def commonElements(self, arr1, arr2, arr3):

        i = j = k = 0
        n1, n2, n3 = len(arr1), len(arr2), len(arr3)
        result = []

        while i < n1 and j < n2 and k < n3:

            if arr1[i] == arr2[j] == arr3[k]:

                if not result or result[-1] != arr1[i]:
                    result.append(arr1[i])

                i += 1
                j += 1
                k += 1

            elif arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1

        if not result:
            return [-1]

        return result


obj = Solution()

arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]

print(obj.commonElements(arr1, arr2, arr3))