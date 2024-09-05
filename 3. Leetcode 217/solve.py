class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      # Create an empty hashmap (or set)
        seen = set()

        # Iterate through each number in the list
        for num in nums:
            if num in seen:  # If the number is already in the set, we found a duplicate
                return True
            seen.add(num)  # Otherwise, add the number to the set

        return False  # If no duplicates were found