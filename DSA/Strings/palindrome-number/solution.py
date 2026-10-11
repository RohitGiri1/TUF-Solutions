class Solution:
    def isPalindrome(self, n):
        if n < 0:
            return False

        num = n
        result = 0

        while num > 0:
            result = result * 10 + num % 10
            num = num // 10

        return n == result