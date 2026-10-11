class Solution:
    def countOddDigit(self, n):
        count = 0
        number = n

        while number>0:
            modulous = number % 10
            number = number // 10
        
            if modulous%2 != 0:
                count+=1
            
        return count  
    