from Solution import Solution


sol = Solution()


def test_one():
    assert sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3, 3, 5, 5, 6, 7]
#                                                           [3, 3, 3, 5, 14, 16]

def test_two():
    assert sol.maxSlidingWindow([1], 1) == [1]
