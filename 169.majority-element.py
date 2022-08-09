#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        myDict = {}
        for i in nums:
            if i not in myDict:
                myDict[i] = 1
            else:
                myDict[i] += 1
        majority = int(len(nums) / 2)
        rkey = 0
        for i in nums:
            if myDict[i] > majority:
                rkey = i
        return rkey 
        
# @lc code=end

