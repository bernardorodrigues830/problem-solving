from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicionario = {}

        for i, n in enumerate(nums): #enumerate: each iteration it does it saves the index and the value
            diferenca = target - n
            if diferenca in dicionario:
                return [dicionario[diferenca], i]
            dicionario[n] = i