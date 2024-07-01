
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int):
        prevMap = {}  # to store the index of each element
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

# Create an instance of the Solution class
sol = Solution()

# Test the function
test = [2, 4, 6, 8]
print(sol.twoSum(test, 12))  # Output: [1, 2]