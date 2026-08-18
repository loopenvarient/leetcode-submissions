class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x= str(x)
        rev= x[::-1]
        if x==rev:
            return True
        else:
            return False