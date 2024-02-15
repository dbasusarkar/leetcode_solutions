from typing import List


class Solution:


    def twoSum(cls, nums: List[int], target: int) -> List[int]:

        num_dictionary = {}        

        for idx in range(len(nums)):
            num2 = target - nums[idx] 

            if num2 in num_dictionary:
                return [idx, num_dictionary[num2]]

            num_dictionary[nums[idx]] = idx
                

