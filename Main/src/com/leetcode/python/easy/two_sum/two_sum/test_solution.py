from Solution import Solution


def test_one():
    sol = Solution()
    assert set(sol.twoSum([2,7,11,15], 9)) == {0, 1}

def test_two():
    sol = Solution()
    assert set(sol.twoSum([3,2,4], 6)) == {1, 2}

def test_three():
    sol = Solution()
    assert set(sol.twoSum([3,3], 6)) == {0, 1}


