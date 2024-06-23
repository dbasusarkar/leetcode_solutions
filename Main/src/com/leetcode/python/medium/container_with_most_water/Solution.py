from typing import List

class Solution:
    """
    11. Container With Most Water
    --------------   
    You are given an integer array `height` of length `n`. 
    There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.

    Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
                 In this case, the max area of water (blue section) the container can contain is 49.

    
    Example 2:
    Input: height = [1,1]
    Output: 1

    Constraints:

    n == height.length
    2 <= n <= 105
    0 <= height[i] <= 104
    """

    def container_with_most_water(self, height: List[int]) -> int:

        left_pointer = 0
        right_pointer = len(height) - 1

        maximum_area = 0
        
        while left_pointer < right_pointer:
            current_width = right_pointer - left_pointer 
            current_area = min (height[left_pointer], height[right_pointer]) * current_width

            maximum_area = max(maximum_area, current_area)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return maximum_area 

