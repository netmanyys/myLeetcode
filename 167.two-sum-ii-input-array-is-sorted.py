#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        pair = {}
        for i,v in enumerate(numbers):
            pair[v] = i
        for i in range(len(numbers)):
            if target - numbers[i] in pair:
                tarI = pair[target-numbers[i]]
                if tarI > i:
                    return [i+1, tarI+1]
                else:
                    return [tarI+1, i+1]

# @lc code=end

