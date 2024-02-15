from typing import List
import math


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum = -math.inf
        sum = 0

        for num in nums: 
            sum = max(num, sum + num)
            largest_sum = max(sum, largest_sum)

        return largest_sum
