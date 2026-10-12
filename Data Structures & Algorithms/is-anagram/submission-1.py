class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1, c2 = collections.Counter(s), collections.Counter(t)
        return c1 == c2
        