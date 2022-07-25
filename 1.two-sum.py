#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for index, num in enumerate(nums):
            mydict[num] = index 
        for index, num in enumerate(nums):
            if (target - num) in nums:
                if mydict[(target - num)] == index:
                    continue
                else:
                    return(index, mydict[(target-num)]) 
# @lc code=end

