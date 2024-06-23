from Solution import Solution

sol = Solution()

def test_one():
    assert sol.container_with_most_water([1,8,6,2,5,4,8,3,7]) == 49 

def test_two():
    assert sol.container_with_most_water([1,1]) == 1

