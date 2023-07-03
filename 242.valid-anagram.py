#
# @lc app=leetcode id=242 lang=python3
#
# 242. Valid Anagram
# Easy
# 9.6K
# 306
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[1], 0)
            countT[t[i]] = 1 + countT.get(t[1], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False 
        return True

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

