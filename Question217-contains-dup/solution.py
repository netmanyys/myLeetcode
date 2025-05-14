class Solution:
    def containsDuplicate(self, nums):
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] = hashmap[i] + 1
                return True
        return False


sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))
print(sol.containsDuplicate([1,2,3,4]))

# Time complexity O(n)
# Space complexity O(n)