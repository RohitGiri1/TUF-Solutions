class Solution:
    def countDigit(self, n):
        if(n == 0):
            return 1
        count = 0
        number = n
        while number>0:
            number = number//10
            count+=1

        return count