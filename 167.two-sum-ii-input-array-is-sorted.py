#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#


class Solution(object):
    def twoSum(self, numbers, target):
        mydict = {}
        for i,v in enumerate(numbers):
            mydict[v] = i
        for i in range(len(numbers)):
            if target - numbers[i] in mydict:
                tar1 = mydict[target - numbers[i]]
                if i > tar1:
                    return (tar1+1, i+1)
                else:
                    return (i+1, tar1+1)


# @lc code=end

