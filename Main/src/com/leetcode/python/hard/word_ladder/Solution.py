from typing import List
from typing import Deque 
from typing import Dict 
from typing import Any
from collections import defaultdict
from collections import deque 

class Solution:
    """
    127. Word Ladder 
    --------------
    A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words 
    `beginWord -> s_1 -> s_2 -> ... -> s_k` such that:

    - Every adjacent pair of words differs by a single letter.
    - Every `s_i` for `1 <= i <= k` is in wordList. Note that `beginWord` does not need to be in `wordList`.
    - `s_k == endWord` 

    Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, 
    return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or `0` if no such sequence exists.

    Example 1:
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
    Output: 5
    Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

    Example 2:
    Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
    Output: 0
    Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

    Constraints:
    - '1 <= beginWord.length <= 10'
    - `endWord.length == beginWord.length` 
    - `1 <= wordList.length <= 5000`
    - `wordList[i].length == beginWord.length`
    - `beginWord`, `endWord`, and `wordList[i]` consist of lowercase English letters.
    - `beginWord != endWord`
    - All the words in `wordList` are unique.
    """
    
    def __init__(self, ):
        self.length: int = 0
        self.all_combined_dict: Dict[str, List[str]] = defaultdict(list)

    def visitedWords(
        self,
        queue: Deque[str],
        visited_first: Dict[str, int],
        visited_second: Dict[str, int]
    ) -> Any:
        queue_size: int = len(queue)

        for idx in range(queue_size):
            current_word: str = queue.popleft()
            
            for i in range(self.length):
                intermed_combination: str = (current_word[:i] + "#" + current_word[i+1:])

                for word in self.all_combined_dict[intermed_combination]:
                    if word in visited_second:
                        return visited_first[current_word] + visited_second[word]
                    
                    if word not in visited_first:
                        visited_first[word] = visited_first[current_word] + 1
                        queue.append(word)

        return None            

    def word_ladder(
        self, 
        beginWord, 
        endWord,
        wordList 
    ) -> int:

        if (
            not beginWord or
            not endWord or
            not wordList or
            endWord not in wordList
        ):
            return 0

        self.length = len(beginWord)
        result: Any = None
        queue_front: Deque[str] = deque([beginWord])
        queue_back: Deque[str] = deque([endWord])
        visitd_front: Dict[str, int] = {beginWord: 1}
        visitd_back: Dict[str, int] = {endWord: 1}

        for word in wordList:
            for idx in range(self.length):
                self.all_combined_dict[word[:idx] + "#" + word[idx+1:]].append(word)

        while queue_front and queue_back:
            if len(queue_front) <= len(queue_back):
                result = self.visitedWords(queue_front, visitd_front, visitd_back)
            else:
                result = self.visitedWords(queue_back, visitd_back, visitd_front)

            if result:
                return result

        return 0

