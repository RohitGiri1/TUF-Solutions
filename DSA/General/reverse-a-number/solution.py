class Solution:
    def reverseNumber(self, n):
        if(n==0):
            return 0
        number = n
        numList = []
        while number > 0:
            numList.append(number%10)
            number = number // 10
            index = len(numList)-1
            result =""
    
        for i in numList :
            result = result + str(i)


        return int(result)