# check-if-word-is-valid-after-substitutions
# https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
# Language: python

class Solution:
    def isValid(self, s: str) -> bool:
        s1 = ""
        while s1 != s:
            s, s1 = s.replace("abc", ""), s
        return s == ""