from Solution import Solution


sol = Solution()


def test_one():
    assert sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6 


def test_two():
    assert sol.maxSubArray([1]) == 1


def test_three():
    assert sol.maxSubArray([5,4,-1,7,8]) == 23
