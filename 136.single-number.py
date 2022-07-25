#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums:
            return
        myDict = {}
        for i in nums:
            if i not in myDict:
                myDict[i] = 1
            else:
                myDict[i] += 1
        for i in nums:
            if myDict[i] == 1:
                return i
            

        
# @lc code=end

