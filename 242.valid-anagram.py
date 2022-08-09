#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)
        a.sort()
        b.sort()
        return a == b
# @lc code=end

