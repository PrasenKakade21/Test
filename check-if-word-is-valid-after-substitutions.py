# 1003. Check If Word Is Valid After Substitutions
# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
# Language: python

class Solution:class Solution:
    def isValid(self, s: str) -> bool:    def isValid(self, s: str) -> bool:
        s1 = ""        s1 = ""
        while s1 != s:        while s1 != s:
            s, s1 = s.replace("abc", ""), s            s, s1 = s.replace("abc", ""), s
        return s == ""        return s == ""