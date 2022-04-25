class Solution:
    def isPalindrome(self, x: int) :
        x = str(x)
        n =  x[::-1]
        
        if n == x:
            return True
        return False
