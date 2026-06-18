from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length <= 1:
            return nums
        else:
            pivot = nums.pop()

        items_greater = []
        items_lower = []

        for item in nums:
            if item > pivot:
                items_greater.append(item)

            else:
                items_lower.append(item)

        return self.sortArray(items_lower) + [pivot] + self.sortArray(items_greater)    