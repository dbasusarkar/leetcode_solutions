from Solution import Solution

sol = Solution()

def test_one():
    assert sol.word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5 

def test_two():
    assert sol.word_ladder("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
