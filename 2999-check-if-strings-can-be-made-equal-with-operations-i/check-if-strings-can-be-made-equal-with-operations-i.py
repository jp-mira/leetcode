class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        #both strings have the same number of length
        n = len(s1)
        
        #set dictionary which count the number for odd and even indices of s1 and s2
        e1, o1 = defaultdict(int), defaultdict(int)
        e2, o2 = defaultdict(int), defaultdict(int)

        for i in range(n):
            if i % 2 == 0:
                e1[s1[i]] += 1
                e2[s2[i]] += 1
            else:
                o1[s1[i]] += 1
                o2[s2[i]] += 1

        """
        if the count of the characters are the same based on the indices, 
        return true, else false
        """
        
        return e1 == e2 and o1 == o2