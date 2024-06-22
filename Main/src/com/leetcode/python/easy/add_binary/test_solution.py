from Solution import Solution

sol = Solution()

def test_one():
    assert sol.addBinary("11", "1") == "100"

def test_two():
    assert sol.addBinary("1010", "1011") == "10101"
