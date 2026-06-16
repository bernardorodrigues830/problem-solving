from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}

        for i, n in enumerate(nums): #enumerate: each iteration it does it saves the index and the value
            diference = target - n
            if diference in dictionary:
                return [dictionary[diference], i]
            dictionary[n] = i