from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]  #nums[len(nums) // 2]: it gets exactly the middle index
    
