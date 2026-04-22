class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        output = []

        def count_changes(word1, word2):
            changes = 0
            for w1, w2 in zip(word1, word2):
                if w1 != w2:
                    changes += 1
                if changes > 2:
                    return changes
            return changes
        
        for query in queries:
            for word in dictionary:
                if len(query) == len(word) and count_changes(query, word) <= 2:
                    output.append(query)
                    break
        return output
        


        