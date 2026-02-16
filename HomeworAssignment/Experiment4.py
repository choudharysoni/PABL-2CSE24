class Solution:
    def findUnion(self,a,b):
        Union=set()

        for x in a:
            Union.add(x)


        for x in b:
            Union.add(x)


        return list(Union)




a=[1, 2, 3, 2, 1]
b=[3, 2, 2, 3, 3, 2]
obj=Solution()
ans = obj.findUnion(a, b)
ans.sort()
print(ans)