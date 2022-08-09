#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for i in s:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1
        for e in t:
            if e not in hashmap:
                return False
            hashmap[e] -= 1
        for key in hashmap:
            if hashmap[key] != 0:
                return False
        return True
# @lc code=end

