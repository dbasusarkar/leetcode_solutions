from collections import deque
from typing import List


class Solution:
    

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        double_ended_queue = deque()
        sliding_window_max_value_list = []
        
        for idx, value in enumerate(nums):

            while double_ended_queue and nums[double_ended_queue[-1]] <= value:
                double_ended_queue.pop()

            double_ended_queue.append(idx)

            if double_ended_queue[0] == idx - k:
                double_ended_queue.popleft()

            if idx >= k - 1:
                sliding_window_max_value_list.append(nums[double_ended_queue[0]])

        return sliding_window_max_value_list
