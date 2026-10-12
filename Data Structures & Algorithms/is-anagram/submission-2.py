class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # c1, c2 = collections.Counter(s), collections.Counter(t)
        # return c1 == c2
        # _____________
        if len(s) != len(t):
            return False

        d1, d2 = {}, {}
        for a, b in zip(s, t):
            if a not in d1:
                d1[a] = 0
            d1[a] +=1
            if b not in d2:
                d2[b] = 0
            d2[b] +=1

        return d1 == d2
        