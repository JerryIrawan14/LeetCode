class Solution:
    def findDisappearedNumbers(self, nums):        
        ans, seen = [], [False]*(len(nums)+1)
        for c in nums: seen[c] = True
        for i in range(1, len(nums)+1):
            if not seen[i]:
                ans.append(i)
        return ans