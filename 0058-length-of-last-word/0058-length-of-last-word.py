class Solution:
    def lengthOfLastWord(self, s: str):
        words= s.split()
        x= words[-1]
        return len(x)

        