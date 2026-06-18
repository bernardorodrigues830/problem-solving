from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)  #no need to check if the key exists

        for s in strs:  #s = temporary variable
            sorted_s = tuple(sorted(s))  #tuples are immutable, therefore they can be used as keys.
            anagram_map[sorted_s].append(s)

        return list(anagram_map.values())